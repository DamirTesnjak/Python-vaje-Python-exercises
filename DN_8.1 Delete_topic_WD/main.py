#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.topic import TopicAdd, TopicDetails, DeleteTopic
from handlers.comments import AddComment
from workers.email_new_comment import EmailNewCommentWorker

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>/details', TopicDetails, name="topic_details"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', DeleteTopic, name="topic_delete"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', AddComment, name="comment-add"),
    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker, name="task-email-new-comment")

], debug=True)
