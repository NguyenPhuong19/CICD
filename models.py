from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    major = db.Column(db.String(100))
    gpa = db.Column(db.Float)

    def __repr__(self):
        return f'<Student {self.name}>'
