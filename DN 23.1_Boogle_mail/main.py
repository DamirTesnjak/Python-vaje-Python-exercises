#!/usr/bin/env python
# -*- coding: UTF-8 -*

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import jinja2
import webapp2
from models import *
from hashlib import sha512


senderEmail = ""
userEmail = ""
userPassword = ""

def deciphering(text):
    decipheredText = ""
    for letter in text:
        if letter in "čČšŠžŽ":
            decipheredText += letter
        else:
            decipheredText += chr(ord(letter) - 2)
    return decipheredText

def IfInboxClicked():
    return senderEmail

def IfSentClicked():
    return userEmail

def messageUserExsist():
    return "User already exsist. <br>Please sign in with different email and password.<br><br>OR<br><br>No email or password. Both fields MUST be filled!"

def notFind():
    return "Oops! Can't find you! Try again or create a new account."

choice = ""
emailList = ""

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)
jinja_env.globals['deciphering'] = deciphering
jinja_env.globals['IfInboxClicked'] = IfInboxClicked
jinja_env.globals['IfSentClicked'] = IfSentClicked


# Sifriranje sporocila zaradi varnostnih razlogov
def ciphering(text):
    cipheredText = ""
    for letter in text:
        if letter in "čČšŠžŽ":
            cipheredText += letter
        else:
            cipheredText += chr(ord(letter) + 2)
    return cipheredText

class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):
        params = {}
        params["logORsign"] = "login"
        params["button"] = "Login"
        params["message"] = "Login in your Boogle account"
        params["visibility"] = ""
        params["notice"] = ""
        return self.render_template("boogle_login.html", params=params)

class SignForm(BaseHandler):
    def get(self):
        params = {}
        params["logORsign"] = "new_user"
        params["button"] = "Sign in"
        params["message"] = "Sign in your Boogle account"
        params["visibility"] = "hidden"
        params["notice"] = ""
        return self.render_template("boogle_login.html", params=params)

class NewUser(BaseHandler):
    def post(self):

        global choice
        choice ="Inbox"

        global userEmail
        userEmail = self.request.get("user")
        global senderEmail
        senderEmail = str(userEmail)
        global userPassword
        userPassword = self.request.get("password")

        idUser = sha512(str(userEmail) + str(userPassword)).hexdigest()
        UsersList = DatabaseOfUsers.query(DatabaseOfUsers.idUser == idUser).fetch()
        user = DatabaseOfUsers(idUser=idUser)

        if len(UsersList) == 0:
            user.put()
        else:
            for item in UsersList:
                if idUser in item.idUser:
                    return self.redirect_to("userExsist")
                else:
                    user.put()
        return self.redirect_to("list")

class userExsist(BaseHandler):
    def get(self):
        params = {}
        params["logORsign"] = "new_user"
        params["button"] = "Sign in"
        params["message"] = "Sign in your Boogle account"
        params["visibility"] = "hidden"
        params["notice"] = messageUserExsist()
        return self.render_template("boogle_login.html", params=params)

class Login(BaseHandler):
    def post(self):
        global choice
        choice ="Inbox"

        global userEmail
        userEmail = self.request.get("user")
        global senderEmail
        senderEmail = str(userEmail)
        global userPassword
        userPassword = self.request.get("password")

        idUser = sha512(str(userEmail) + str(userPassword)).hexdigest()
        UsersList = DatabaseOfUsers.query(DatabaseOfUsers.idUser == idUser).fetch()

        if len(UsersList) == 0:
            return self.redirect_to("notFind")
        else:
            for item in UsersList:
                if idUser not in item.idUser:
                    return self.redirect_to("notFind")

        return self.redirect_to("list")

class NotFindYou(BaseHandler):
    def get(self):
        params = {}
        params["logORsign"] = "login"
        params["button"] = "Login"
        params["message"] = "Login in your Boogle account"
        params["notice"] = notFind()
        return self.render_template("boogle_login.html", params=params)

class Logout(BaseHandler):
    def get(self):
        return self.redirect_to("form")

class AddHandler(BaseHandler):
    def post(self):
        email = self.request.get("email")
        subject = self.request.get("subject")
        text = self.request.get("text")

        if "<script>" in email or "<script>" in text or "<script>" in subject:
            email = email.replace("<script>", "")
            email = email.replace("</script>", "")
            subject = subject.replace("<script>", "")
            subject = subject.replace("</script>", "")
            text = text.replace("<script>", "")
            text = text.replace("</script>", "")

        email = ciphering(email)
        subject = ciphering(subject)
        text = ciphering(text)

        global senderEmail
        senderEmail = ciphering(senderEmail)

        E_mail_Inbox = Inbox(email=email, subject=subject, text=text, senderEmail=senderEmail)
        E_mail_Outbox = Outbox(email=email, subject=subject, text=text, senderEmail=senderEmail)

        E_mail_Inbox.put()
        E_mail_Outbox.put()

        return self.redirect_to("list")

class EmailListHandler(BaseHandler):
    def get(self):
        email = ciphering(userEmail)
        params = {}

        if choice == "Inbox":
            global emailList
            emailList = Inbox.query(Inbox.deleted==False, Inbox.email == email).fetch()
            params["choice"] = choice
            params["recSend"] = "From"
            params["cmd"] = "Delete"
            params["link"] = "_delete"
            params["visibility"] = "hidden"
            params["delete_mode"] = "delete"
            params["delete_mode_name"] = "Delete all"
            params["senderEmail"] = IfInboxClicked()
            params["user"] = userEmail

        elif choice == "Sent":
            global emailList
            emailList = Outbox.query(Outbox.deleted==False, Outbox.senderEmail==email).fetch()
            params["choice"] = choice
            params["recSend"] = "For"
            params["cmd"] = "Delete"
            params["link"] = "_delete"
            params["visibility"] = "hidden"
            params["delete_mode"] = "delete"
            params["delete_mode_name"] = "Delete all"
            params["user"] = userEmail

        else:
            global emailList
            emailList = Inbox.query(Inbox.deleted==True).fetch() + Outbox.query(Inbox.deleted==True).fetch()
            params["choice"] = choice
            params["recSend"] = "Sender"
            params["cmd"] = "Erase"
            params["link"] = "_erase"
            params["cmd_restore"] = "restore"
            params["link_restore"] = "restore"
            params["visibility"] = ""
            params["delete_mode"] = "erase"
            params["delete_mode_name"] = "Erase all"
            params["user"] = userEmail

        params["emailList"] = emailList
        return self.render_template("email_list.html", params=params)

class GetEmailsHandler(BaseHandler):
    def post(self):
        global choice
        choice = self.request.get("choice")
        email = ciphering(userEmail)
        params = {}

        if choice == "Inbox":
            global emailList
            emailList = Inbox.query(Inbox.deleted==False, Inbox.email == email).fetch()
            params["choice"] = choice
            params["recSend"] = "From:"
            params["cmd"] = "Delete"
            params["link"] = "_delete"
            params["visibility"] = "hidden"
            params["delete_mode"] = "delete"
            params["delete_mode_name"] = "Delete all"
            params["senderEmail"] = IfInboxClicked()
            params["user"] = userEmail

        elif choice == "Sent":
            global emailList
            emailList = Outbox.query(Outbox.deleted==False, Outbox.senderEmail==email).fetch()
            params["choice"] = choice
            params["recSend"] = "For:"
            params["cmd"] = "Delete"
            params["link"] = "_delete"
            params["visibility"] = "hidden"
            params["delete_mode"] = "delete"
            params["delete_mode_name"] = "Delete all"
            params["user"] = userEmail

        else:
            global emailList
            emailList = Inbox.query(Inbox.deleted==True).fetch() + Outbox.query(Inbox.deleted==True).fetch()
            params["choice"] = choice
            params["recSend"] = "For:"
            params["cmd"] = "Erase"
            params["link"] = "_erase"
            params["cmd_restore"] = "restore"
            params["link_restore"] = "restore"
            params["visibility"] = ""
            params["delete_mode"] = "erase"
            params["delete_mode_name"] = "Erase all"
            params["user"] = userEmail

        params["emailList"] = emailList
        return self.render_template("email_list.html", params=params)

class DeleteemailHandler(BaseHandler):
    def get(self, email_id):
        email_inbox = Inbox.get_by_id(int(email_id))
        email_outbox = Outbox.get_by_id(int(email_id))
        if email_inbox:
            email_inbox.deleted = True
            email_inbox.put()
        elif email_outbox:
            email_outbox.deleted = True
            email_outbox.put()

        return self.redirect_to("list")

class UndeleteemailHandler(BaseHandler):
    def get(self, email_id):
        email_inbox = Inbox.get_by_id(int(email_id))
        email_outbox = Outbox.get_by_id(int(email_id))

        if email_inbox:
            email_inbox.deleted = False
            email_inbox.put()
        else:
            email_outbox.deleted = False
            email_outbox.put()

        return self.redirect_to("list")

class PermanentlyDeleteemailHandler(BaseHandler):
    def get(self, email_id):
        email_inbox = Inbox.get_by_id(int(email_id))
        email_outbox = Outbox.get_by_id(int(email_id))

        if email_inbox:
            email_inbox.key.delete()

        else:
            email_outbox.key.delete()

        return self.redirect_to("list")

class DeleteTrashHandler(BaseHandler):
    def get(self):
        for item in emailList:
            item.key.delete()
        return self.redirect_to("list")

class deleteAllemailsHandler(BaseHandler):
    def get(self):
        for item in emailList:
            item.deleted = True
            item.put()

        return self.redirect_to("list")

class restoreAllemailsHandler(BaseHandler):
    def get(self):
        for item in emailList:
            item.deleted = False
            item.put()
        return self.redirect_to("list")

class ReadEmailHandler(BaseHandler):
    def get(self, email_id):
        email_inbox = Inbox.get_by_id(int(email_id))
        email_outbox = Outbox.get_by_id(int(email_id))

        if email_inbox:
            email_inbox.read = "Yes"
            email_inbox.put()

        else:
            email_outbox.read = "Yes"
            email_outbox.put()

        return self.redirect_to("list")

class UnReadEmailHandler(BaseHandler):
    def get(self, email_id):
        email_inbox = Inbox.get_by_id(int(email_id))
        email_outbox = Outbox.get_by_id(int(email_id))

        if email_inbox:
            email_inbox.read = "No"
            email_inbox.put()

        else:
            email_outbox.read = "No"
            email_outbox.put()

        return self.redirect_to("list")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="form"),
    webapp2.Route('/email_list', EmailListHandler, name="list"),
    webapp2.Route('/new_user', NewUser),
    webapp2.Route('/signin', SignForm, name="signin"),
    webapp2.Route('/cannot_signin', userExsist, name="userExsist"),
    webapp2.Route('/login', Login),
    webapp2.Route('/nofound', NotFindYou, name="notFind"),
    webapp2.Route('/logout', Logout),
    webapp2.Route('/add', AddHandler),
    webapp2.Route('/getEmail_list', GetEmailsHandler, name="getEmailList"),
    webapp2.Route('/email/<email_id:\d+>/delete', DeleteemailHandler),
    webapp2.Route('/del_all', deleteAllemailsHandler),
    webapp2.Route('/email/<email_id:\d+>/restore', UndeleteemailHandler),
    webapp2.Route('/restore_all', restoreAllemailsHandler),
    webapp2.Route('/email/<email_id:\d+>/permanently_delete', PermanentlyDeleteemailHandler),
    webapp2.Route('/empty_trash', DeleteTrashHandler),
    webapp2.Route('/email/<email_id:\d+>/read', ReadEmailHandler),
    webapp2.Route('/email/<email_id:\d+>/unread', UnReadEmailHandler),

], debug=True)
