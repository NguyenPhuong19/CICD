from flask import Flask
from flask_admin import Admin, BaseView, expose


def create_app():
    app = Flask(__name__)
    admin = Admin(app)
    admin.add_view(
        MyView(name='My View')
    )  # ✅ tách dòng để tránh lỗi E501 (line too long)
    return app


class MyView(BaseView):

    @expose('/')
    def index(self):
        return self.render('index.html')


app = create_app()
