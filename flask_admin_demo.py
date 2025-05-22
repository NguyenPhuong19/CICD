from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from models import db, Student


class MyDashboard(BaseView):
    @expose('/')
    def index(self):
        students = Student.query.all()
        count = len(students)
        max_gpa = max([s.gpa for s in students]) if students else 0
        avg_gpa = round(sum([s.gpa for s in students]) / count, 2) if count > 0 else 0

        majors = {}
        for s in students:
            majors[s.major] = majors.get(s.major, 0) + 1

        return self.render('admin/myview.html',
                           count=count,
                           max_gpa=max_gpa,
                           avg_gpa=avg_gpa,
                           majors=majors)

from flask_admin import AdminIndexView

class MyAdminHome(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/home_admin.html')  # file bạn đã tạo trong templates/admin/


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345678'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    admin = Admin(
    app,
    name='Trang Quản Trị',
    template_mode='bootstrap3',
    index_view=MyAdminHome(name='Home')  # đây là dòng quan trọng bạn đang hỏi
)


    # Giao diện nâng cao
    admin.add_view(MyDashboard(name='📊 Dashboard'))
    admin.add_view(ModelView(Student, db.session, name='🎓 Sinh viên'))

    @app.route('/')
    def home():
        return render_template('index.html')

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
