from google.appengine.ext import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty()
    description = ndb.TextProperty()
    deleted = ndb.BooleanProperty(default=False)
    thumbnail = ndb.StringProperty()
    done = ndb.StringProperty(default="No")
    rating = ndb.StringProperty()
