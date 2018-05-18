from google.appengine.ext import ndb

class DatabaseOfUsers(ndb.Model):
    idUser = ndb.StringProperty()

class Inbox(ndb.Model):
    email = ndb.StringProperty()
    subject = ndb.StringProperty()
    text = ndb.TextProperty()
    senderEmail = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    read = ndb.StringProperty(default="No")


class Outbox(ndb.Model):
    email = ndb.StringProperty()
    subject = ndb.StringProperty()
    text = ndb.TextProperty()
    senderEmail = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    read = ndb.StringProperty(default="No")
