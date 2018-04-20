#!/usr/bin/env python
# -*- coding: UTF-8 -*

import os
import jinja2
import webapp2
import random

'''#---------------da HTML lahko prikaže šumnike in ostalo navlako-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#--------------------------------------------'''

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
        global dictLines
        dictLines = {}          # Prazen dictionary keys=COUNTRIES, value=CAPITAL CITY

        for y in range(3):
            with open("national_capital_cities.txt", 'r') as file:
                lines =file.readlines()                     # Branje vseh vrstic v datoteki
                selectedLine = random.choice(lines)         #Izbira naključne vrstice
                lineAsList = selectedLine.split(",")        #String pretvorimo v 'list', deliminator ','

                dictLines[lineAsList[1][0:]] = lineAsList[2]    #Vnos keys=COUNTRIES, value=CAPITAL CITY v dictionary

        global ordDictKeys
        ordDictKeys = dictLines.keys()         #Dobiti ključe

        global randomIndex
        randomIndex = random.randint(0,2)      #Naključen indeks

        global country
        country = ordDictKeys[randomIndex]    #Dobimo izbrano državo za katero iščemo glavno mesto

        #Izpis vpračanja
        global answerA
        answerA = dictLines[ordDictKeys[0]]

        global answerB
        answerB = dictLines[ordDictKeys[1]]

        global answerC
        answerC = dictLines[ordDictKeys[2]]

        params = {"answerA": u''+ answerA,
                  "answerB": u''+ answerB,
                  "answerC": u''+ answerC,
                  "country": u''+ country,
                  "flag" : u'' + country + ".jpg"}

        return self.render_template("index.html", params=params)

    def post(self):
        answerIndex = {"A": 0, "B": 1, "C": 2} # Dictionary keys=odgovor, value=indeks
        answer = self.request.get("vnos")

        #Preverimo, če je odgovor pravilen
        if answerIndex[answer.upper()] == ordDictKeys.index(country):
            result = "Correct!"
        else:
            result = "Incorrect! It is " + dictLines[ordDictKeys[randomIndex]] + "!"

        params = {"answerA": u''+ answerA,
                  "answerB": u''+ answerB,
                  "answerC": u''+ answerC,
                  "country": u''+ country,
                  "flag" : u'' + country + ".jpg",
                  "result": u''+ result}

        return self.render_template("index.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
