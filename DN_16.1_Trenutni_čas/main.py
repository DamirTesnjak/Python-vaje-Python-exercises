#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime
import time
 

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

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
		params = {"time": datetime.datetime.now().strftime('UTC: %H : %M : %S<br /> Date: %d. %m. %Y')}
		return self.render_template("time.html", params=params)

while True:
	app = webapp2.WSGIApplication([webapp2.Route('/', MainHandler),], debug=True)
	time.sleep(10)
