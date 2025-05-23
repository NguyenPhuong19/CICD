from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from models import db, Student

# các class như MyDashboard và MyAdminHome giữ nguyên...

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345678'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    admin = Admin(app, name='Trang Quản Trị', template_mode='bootstrap3', index_view=MyAdminHome(name='Home'))
    admin.add_view(MyDashboard(name='📊 Dashboard'))
    admin.add_view(ModelView(Student, db.session, name='🎓 Sinh viên'))

    @app.route('/')
    def home():
        return render_template('index.html')

    return app

# 🔥 Đây là dòng cực kỳ quan trọng để gunicorn tìm được biến `app`
app = create_app()

# ✅ Nếu chạy local
if __name__ == '__main__':
    app.run(debug=True)
