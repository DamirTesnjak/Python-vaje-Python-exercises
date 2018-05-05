#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Movie

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
        return self.render_template("intro.html")

class AddHandler(BaseHandler):
    def post(self):
        title = self.request.get("title")
        rating = self.request.get("rating")
        thumbnail = self.request.get("thumbnail")
        description = self.request.get("description")

        if "<script>" in title or "<script>" in description or "<script>" in rating:
            title = title.replace("<script>", "")
            title = title.replace("</script>", "")
            thumbnail = description.replace("<script>", "")
            thumbnail = description.replace("</script>", "")
            description = description.replace("<script>", "")
            description = description.replace("</script>", "")
            rating = rating.replace("<script>", "")
            rating = rating.replace("</script>", "")

        movie = Movie(title=title, rating=rating, thumbnail=thumbnail, description=description)

        movie.put()
        return self.redirect_to("list")

class EditHandler(BaseHandler):
    def get(self, movie_id):
        movie = Movie.get_by_id(int(movie_id))

        params = {"movie" : movie}

        return self.render_template("edit_movie.html", params=params)

    def post(self, movie_id):
        title = self.request.get("title")
        rating = self.request.get("rating")
        description = self.request.get("description")
        movie = Movie.get_by_id(int(movie_id))

        if "<script>" in title or "<script>" in description or "<script>" in rating:
            title = title.replace("<script>", "")
            title = title.replace("</script>", "")
            description = description.replace("<script>", "")
            description = description.replace("</script>", "")
            rating = rating.replace("<script>", "")
            rating = rating.replace("</script>", "")

        movie.title = title
        movie.rating = rating
        movie.description = description
        movie.put()
        return self.redirect_to("list")

class MovieListHandler(BaseHandler):
    def get(self):
        movieList = Movie.query(Movie.deleted==False).fetch()
        params = {"movieList": movieList}
        return self.render_template("movie_list.html", params=params)

class DeleteMovieHandler(BaseHandler):
    def get(self, movie_id):
        movie = Movie.get_by_id(int(movie_id))
        movie.deleted = True
        movie.put()
        return self.redirect_to("list")

class DeletedMoviesHandler(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==True).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

class UndeleteMovieHandler(BaseHandler):
    def get(self, movie_id):
        movie = Movie.get_by_id(int(movie_id))
        movie.deleted = False
        movie.put()
        return self.redirect_to("trash")

class PermanentlyDeleteMovieHandler(BaseHandler):
    def get(self, movie_id):
        movie = Movie.get_by_id(int(movie_id))
        movie.key.delete()
        return self.redirect_to("trash")

class DeleteTrashHandler(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==True).order(Movie.title).fetch()
        for item in movieListDeleted:
            item.key.delete()
        return self.redirect_to("trash")

class deleteAllMoviesHandler(BaseHandler):
    def get(self):
        movieList = Movie.query(Movie.deleted==False).fetch()
        for item in movieList:
            item.deleted = True
            item.put()
        return self.redirect_to("list")

class restoreAllMoviesHandler(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==True).fetch()
        for item in movieListDeleted:
            item.deleted = False
            item.put()
        return self.redirect_to("trash")

class DoneMovieHandler(BaseHandler):
    def get(self, movie_id):
        movie = Movie.get_by_id(int(movie_id))
        movie.done = "Yes"
        movie.put()
        return self.redirect_to("list")

class SortMovieListByTitleUP(BaseHandler):
    def get(self):
        movieList = Movie.query(Movie.deleted==False).order(Movie.title).fetch()
        params = {"movieList": movieList}
        return self.render_template("movie_list.html", params=params)

class SortMovieListByTitleDOWN(BaseHandler):
    def get(self):
        movieList = Movie.query(Movie.deleted==False).order(-Movie.title).fetch()
        params = {"movieList": movieList}
        return self.render_template("movie_list.html", params=params)

class SortMovieListByRatingUP(BaseHandler):
    def get(self):
        movieList = Movie.query(Movie.deleted==False).order(Movie.rating).fetch()
        params = {"movieList": movieList}
        return self.render_template("movie_list.html", params=params)

class SortMovieListByRatingDOWN(BaseHandler):
    def get(self):
        movieList = Movie.query(Movie.deleted==False).order(-Movie.rating).fetch()
        params = {"movieList": movieList}
        return self.render_template("movie_list.html", params=params)

class SortMovieListByStatusUP(BaseHandler):
    def get(self):
        movieList = Movie.query(Movie.deleted==False).order(Movie.done).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

class SortMovieListByStatusDOWN(BaseHandler):
    def get(self):
        movieList = Movie.query(Movie.deleted==False).order(-Movie.done).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

class SortMovieListByTitleUP_del(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==False).order(Movie.title).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

class SortMovieListByTitleDOWN_del(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==False).order(-Movie.title).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

class SortMovieListByRatingUP_del(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==False).order(Movie.rating).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

class SortMovieListByRatingDOWN_del(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==False).order(-Movie.rating).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

class SortMovieListByStatusUP_del(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==False).order(Movie.done).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

class SortMovieListByStatusDOWN_del(BaseHandler):
    def get(self):
        movieListDeleted = Movie.query(Movie.deleted==False).order(-Movie.done).fetch()
        params = {"movieListDeleted": movieListDeleted}
        return self.render_template("deleted_Movie_list.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/add', AddHandler),
    webapp2.Route('/movie_list', MovieListHandler, name="list"),
    webapp2.Route('/movie/<movie_id:\d+>/delete', DeleteMovieHandler),
    webapp2.Route('/movie/<movie_id:\d+>/edit', EditHandler),
    webapp2.Route('/del_all', deleteAllMoviesHandler),
    webapp2.Route('/trash', DeletedMoviesHandler, name="trash"),
    webapp2.Route('/movie/<movie_id:\d+>/restore', UndeleteMovieHandler),
    webapp2.Route('/restore_all', restoreAllMoviesHandler),
    webapp2.Route('/movie/<movie_id:\d+>/permanently_delete', PermanentlyDeleteMovieHandler),
    webapp2.Route('/empty_trash', DeleteTrashHandler),
    webapp2.Route('/movie/<movie_id:\d+>/done', DoneMovieHandler),
    webapp2.Route('/sortTitleUP', SortMovieListByTitleUP),
    webapp2.Route('/sortTitleDOWN', SortMovieListByTitleDOWN),
    webapp2.Route('/sortRatingUP', SortMovieListByRatingUP),
    webapp2.Route('/sortRatingDOWN', SortMovieListByRatingDOWN),
    webapp2.Route('/sortStatusUP', SortMovieListByStatusUP),
    webapp2.Route('/sortStatusDOWN', SortMovieListByStatusDOWN),
    webapp2.Route('/sortTitleUP_del', SortMovieListByTitleUP_del),
    webapp2.Route('/sortTitleDOWN_del', SortMovieListByTitleDOWN_del),
    webapp2.Route('/sortRatingUP_del', SortMovieListByRatingUP_del),
    webapp2.Route('/sortRatingDOWN_del', SortMovieListByRatingDOWN_del),
    webapp2.Route('/sortStatusUP_del', SortMovieListByStatusUP_del),
    webapp2.Route('/sortStatusDOWN_del', SortMovieListByStatusDOWN_del),

], debug=True)
