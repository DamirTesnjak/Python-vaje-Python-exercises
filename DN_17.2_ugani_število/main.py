#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import jinja2
import webapp2
import random

#---------------da HTML lahko prikaže šumnike-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#--------------------------------------------


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
        return self.render_template("index.html")

    def post(self):
        # Naključno iskno število
        secret = random.randint(1, 10)

        # Input
        guess = int(self.request.get("vnos"))

        # Pogoji in izpis
        try:
            if secret == guess and guess >= 1 and guess <= 10:
                params = {"result": "Zmagali ste! Uganili ste število " + str( secret ) + "!"}

            elif secret != guess and guess >= 1 and guess <= 10:
                params = {"result": "Izgubili ste! Uganiti ste morali število " + str( secret ) + "!"}

            else:
                params = {"result": "Napaka! Vnesli ste število izven intervala!"}
        except ValueError:
            params = {"result": "Vnesite število!"}

        return self.render_template("index.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
