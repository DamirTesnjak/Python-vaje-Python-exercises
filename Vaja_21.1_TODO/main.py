#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Task

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
        deadline = self.request.get("deadline")
        description = self.request.get("description")

        if "<script>" in title or "<script>" in description or "<script>" in deadline:
            title = title.replace("<script>", "")
            title = title.replace("</script>", "")
            description = description.replace("<script>", "")
            description = description.replace("</script>", "")
            deadline = deadline.replace("<script>", "")
            deadline = deadline.replace("</script>", "")

        task = Task(title=title, deadline=deadline, description=description)

        task.put()
        return self.redirect_to("list")

class EditHandler(BaseHandler):
    def get(self, task_id):
        task = Task.get_by_id(int(task_id))

        params = {"task" : task}

        return self.render_template("edit_task.html", params=params)

    def post(self, task_id):
        title = self.request.get("title")
        deadline = self.request.get("deadline")
        description = self.request.get("description")
        task = Task.get_by_id(int(task_id))

        if "<script>" in title or "<script>" in description or "<script>" in deadline:
            title = title.replace("<script>", "")
            title = title.replace("</script>", "")
            description = description.replace("<script>", "")
            description = description.replace("</script>", "")
            deadline = deadline.replace("<script>", "")
            deadline = deadline.replace("</script>", "")

        task.title = title
        task.deadline = deadline
        task.description = description
        task.put()
        return self.redirect_to("list")

class TaskListHandler(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class DeleteTaskHandler(BaseHandler):
    def get(self, task_id):
        task = Task.get_by_id(int(task_id))
        task.deleted = True
        task.put()
        return self.redirect_to("list")

class DeletedTasksHandler(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==True).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

class UndeleteTaskHandler(BaseHandler):
    def get(self, task_id):
        task = Task.get_by_id(int(task_id))
        task.deleted = False
        task.put()
        return self.redirect_to("trash")

class PermanentlyDeleteTaskHandler(BaseHandler):
    def get(self, task_id):
        task = Task.get_by_id(int(task_id))
        task.key.delete()
        return self.redirect_to("trash")

class DeleteTrashHandler(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==True).order(Task.title).fetch()
        for item in taskListDeleted:
            item.key.delete()
        return self.redirect_to("trash")

class deleteAllTasksHandler(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).fetch()
        for item in taskList:
            item.deleted = True
            item.put()
        return self.redirect_to("task_list")

class restoreAllTasksHandler(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==True).fetch()
        for item in taskListDeleted:
            item.deleted = False
            item.put()
        return self.redirect_to("trash")

class DoneTaskHandler(BaseHandler):
    def get(self, task_id):
        task = Task.get_by_id(int(task_id))
        task.done = True
        task.put()
        return self.redirect_to("task_list")

class SortTaskListByTitleUP(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).order(Task.title).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class SortTaskListByTitleDOWN(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).order(-Task.title).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class SortTaskListByDeadlineUP(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).order(Task.deadline).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class SortTaskListByDeadlineDOWN(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).order(-Task.deadline).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class SortTaskListByDateTimeUP(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).order(Task.date).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class SortTaskListByDateTimeDOWN(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).order(-Task.date).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class SortTaskListByDateStatusUP(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).order(Task.done).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class SortTaskListByDateStatusDOWN(BaseHandler):
    def get(self):
        taskList = Task.query(Task.deleted==False).order(-Task.done).fetch()
        params = {"taskList": taskList}
        return self.render_template("task_list.html", params=params)

class SortTaskListByTitleUP_del(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==False).order(Task.title).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

class SortTaskListByTitleDOWN_del(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==False).order(-Task.title).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

class SortTaskListByDeadlineUP_del(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==False).order(Task.deadline).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

class SortTaskListByDeadlineDOWN_del(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==False).order(-Task.deadline).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

class SortTaskListByDateTimeUP_del(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==False).order(Task.date).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

class SortTaskListByDateTimeDOWN_del(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==False).order(-Task.date).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

class SortTaskListByDateStatusUP_del(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==False).order(Task.done).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

class SortTaskListByDateStatusDOWN_del(BaseHandler):
    def get(self):
        taskListDeleted = Task.query(Task.deleted==False).order(-Task.done).fetch()
        params = {"taskListDeleted": taskListDeleted}
        return self.render_template("deleted_Task_list.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/add', AddHandler),
    webapp2.Route('/task_list', TaskListHandler, name="list"),
    webapp2.Route('/task/<task_id:\d+>/delete', DeleteTaskHandler),
    webapp2.Route('/task/<task_id:\d+>/edit', EditHandler),
    webapp2.Route('/del_all', deleteAllTasksHandler),
    webapp2.Route('/trash', DeletedTasksHandler, name="trash"),
    webapp2.Route('/task/<task_id:\d+>/restore', UndeleteTaskHandler),
    webapp2.Route('/restore_all', restoreAllTasksHandler),
    webapp2.Route('/task/<task_id:\d+>/permanently_delete', PermanentlyDeleteTaskHandler),
    webapp2.Route('/empty_trash', DeleteTrashHandler),
    webapp2.Route('/task/<task_id:\d+>/done', DoneTaskHandler),
    webapp2.Route('/sortTitleUP', SortTaskListByTitleUP),
    webapp2.Route('/sortTitleDOWN', SortTaskListByTitleDOWN),
    webapp2.Route('/sortDeadlineUP', SortTaskListByDeadlineUP),
    webapp2.Route('/sortDeadlineDOWN', SortTaskListByDeadlineDOWN),
    webapp2.Route('/sortDateUP', SortTaskListByDateTimeUP),
    webapp2.Route('/sortDateDOWN', SortTaskListByDateTimeDOWN),
    webapp2.Route('/sortStatusUP', SortTaskListByDateStatusUP),
    webapp2.Route('/sortStatusDOWN', SortTaskListByDateStatusDOWN),
    webapp2.Route('/sortTitleUP_del', SortTaskListByTitleUP_del),
    webapp2.Route('/sortTitleDOWN_del', SortTaskListByTitleDOWN_del),
    webapp2.Route('/sortDeadlineUP_del', SortTaskListByDeadlineUP_del),
    webapp2.Route('/sortDeadlineDOWN_del', SortTaskListByDeadlineDOWN_del),
    webapp2.Route('/sortDateUP_del', SortTaskListByDateTimeUP_del),
    webapp2.Route('/sortDateDOWN_del', SortTaskListByDateTimeDOWN_del),
    webapp2.Route('/sortStatusUP_del', SortTaskListByDateStatusUP_del),
    webapp2.Route('/sortStatusDOWN_del', SortTaskListByDateStatusDOWN_del),

], debug=True)
