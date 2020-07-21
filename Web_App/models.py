from Web_App import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    profile_pic = db.Column(db.String(20), nullable=False, default='default_user.jpg')
    password = db.Column(db.String(60), nullable=False)
    cgpa = db.Column(db.String(5), nullable=False)

    result = db.relationship('Result', backref='user_result', lazy=True)

    def __repr__(self):
        return f"User('{self.username}'"


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.Text, nullable=False)
    gpa = db.Column(db.String(5), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Result('{self.name}')"


class ActiveGroup(db.Model):
    # relation containing users in group, unique name, posts relation
    pass
