from handlers.base import BaseHandler
from google.appengine.api import users
from models.models import Topic, Comment
from google.appengine.api import memcache
import uuid

class AddComment(BaseHandler):
    def post(self, topic_id):
        csrf_token = self.request.get("csrf_token")
        mem_token = memcache.get(key=csrf_token)  # find if this CSRF exists in memcache

        if not mem_token:  # if token does not exist in memcache, write the following message
            return self.write("Attack attempt detected...")

        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        topic = Topic.get_by_id(int(topic_id))
        text = self.request.get("comment")

        Comment.create(content=text, user=user, topic=topic)

        return self.redirect_to("topic_details", topic_id=topic.key.id())
