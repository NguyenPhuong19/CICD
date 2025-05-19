from flask_admin import AdminIndexView, expose
from models import Student

class MyAdminHome(AdminIndexView):
    @expose('/')
    def index(self):
        students = Student.query.all()
        count = len(students)
        max_gpa = max([s.gpa for s in students]) if students else 0
        avg_gpa = round(sum([s.gpa for s in students]) / count, 2) if count > 0 else 0

        majors = {}
        for s in students:
            majors[s.major] = majors.get(s.major, 0) + 1

        return self.render('admin/home_admin.html',  # ← file HTML của bạn
                           count=count,
                           max_gpa=max_gpa,
                           avg_gpa=avg_gpa,
                           majors=majors)  # ← phải có dòng này
