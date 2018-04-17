#!/usr/bin/env python
# -*- coding: UTF-8 -*

import os
import jinja2
import webapp2

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

class ResultHandler(BaseHandler):
    def post(self):
        hairColor = {
            "blond": "TTAGCTATCGC",
            "črna": "CCAGCAATCGC",
            "rjava": "GCCAGTGCCG"
        }

        facialShape = {
            "kvadraten": "GCCACGG",
            "okrogel": "ACCACAA",
            "ovalen": "AGGCCTCA"
        }

        eyeColor = {
            "modra": "TTGTGGTGGC",
            "zelena": "GGGAGGTGGC",
            "rjava": "AAGTAGTGAC"
        }

        Gender = {
            "ženski": "TGAAGGACCTTC",
            "moški": "TGCAGGAACTTC"
        }

        Race = {
            "belec": "AAAACCTCA",
            "črnec": "CGACTACAG",
            "azijec": "CGCGGGCCG"
        }
        stringDNA = self.request.get("DNA-input")

        def getPropety(dictionary):
            dict_to_list = dictionary.keys() # shrani kljuce (keys) kot novi seznam.
            dict_to_list.sort()

            for key in dict_to_list:
                if dictionary[key] in stringDNA:
                    return key

        params = {"spol" : getPropety(Gender),
                  "barva_las": getPropety(hairColor),
                  "obraz": getPropety(facialShape),
                  "barva_oci": getPropety(eyeColor),
                  "rasa": getPropety(Race)}

        return self.render_template("result.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/result', ResultHandler),

], debug=True)
