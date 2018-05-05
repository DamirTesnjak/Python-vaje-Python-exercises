from google.appengine.ext import ndb

class Message(ndb.Model):
    title = ndb.StringProperty()
    message = ndb.TextProperty()
    date = ndb.DateProperty(auto_now_add=True)
    time = ndb.TimeProperty(auto_now_add=True)
