from google.appengine.ext import ndb

class Task(ndb.Model):
    title = ndb.StringProperty()
    description = ndb.TextProperty()
    deleted = ndb.BooleanProperty(default=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
    done = ndb.BooleanProperty(default=False)
    deadline = ndb.StringProperty()
