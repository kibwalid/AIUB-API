from flask import (
    request,
    redirect,
    render_template,
    url_for,
)
from Web_App.forms import (
    LoginForm,
    RegisterForm,
)
from Web_App import app
from Vues_Con import vueCon


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        vue = vueCon.Info()
        name = vue.login(username=form.username.data, password=form.password.data)
        if name is None:
            return "VUES Login Error!"
        course = vue.get_notice_data("https://www.aiub.edu/general-instructions-of-online-classes")
        # course = course.to_html()
        # return render_template('home.html', name=name, data=course)
        return f"{course['Title']}"
    return render_template('login.html', form=form, title="Login")


@app.route('/register')
def register():
    form = RegisterForm()
    pass
