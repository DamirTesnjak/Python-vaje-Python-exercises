#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.topic import TopicAdd, TopicDetails
from handlers.comments import AddComment

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>/details', TopicDetails, name="topic_details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', AddComment, name="comment-add"),
], debug=True)
