#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("Home_guestbook.html")


class SendMessageHandler(BaseHandler):
    def post(self):
        name = self.request.get("name")
        email = self.request.get("email")
        message = self.request.get("message")

        if "<script>" in message:
            message = message.replace("<script>", "")
            message = message.replace("</script>", "")

        cardMessage = Message(name=name, email=email, message=message)

        cardMessage.put()
        return self.redirect_to("main")

class MessagesHandler(BaseHandler):
    def get(self):
        listMessages = Message.query(Message.deleted==False).fetch()
        params = {"listMessages" : listMessages}
        return self.render_template("messages.html", params=params)


class DeletedMessagesHandler(BaseHandler):
    def get(self):
        listMessages = Message.query(Message.deleted==True).fetch()
        params = {"listMessages" : listMessages}
        return self.render_template("Messages_deleted.html", params=params)


class IRR_DeleteMessageHandler(BaseHandler): #Ireversible deletion
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("irr_deleted.html", params=params)

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))
        message.key.delete()
        return self.redirect_to("messages_deleted")


class RestoreMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        return self.render_template("Messages_deleted.html")

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))
        message.deleted = False
        message.put()
        return self.redirect_to("messages")


class ShowMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("Show_message.html", params=params)


class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("Edit_message.html", params=params)

    def post(self, message_id):
        message = self.request.get("message")
        message_obj = Message.get_by_id(int(message_id))

        if "<script>" in message:
            message = message.replace("<script>", "")
            message = message.replace("</script>", "")

        message_obj.message = message
        message_obj.put()
        return self.redirect_to("messages")


class DeleteMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("delete_message.html", params=params)

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))
        message.deleted = True
        message.put()
        return self.redirect_to("messages")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main"),
    webapp2.Route('/temp', SendMessageHandler),
    webapp2.Route('/messages', MessagesHandler, name="messages"),
    webapp2.Route('/message/<message_id:\d+>', ShowMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteMessageHandler),
    webapp2.Route('/messages_del', DeletedMessagesHandler, name="messages_deleted"),
    webapp2.Route('/message/<message_id:\d+>/irr_deleted', IRR_DeleteMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/restore', RestoreMessageHandler),
], debug=True)
