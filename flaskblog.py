from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fbc1fa79f4d8b12baa1d78826179aaff'

posts = [{
    'title': 'Blog Post 1',
    'author': 'Abou Bamba',
    'date_posted': 'April 23, 2023',
    'content': 'First Blog Post'
}, {
    'title': 'Blog Post 2',
    'author': 'Jane Doe',
    'date_posted': 'June 9, 2023',
    'content': 'Second Blog Post'
}]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You successfully log in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Check your email and password', 'danger')
    return render_template('Login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
