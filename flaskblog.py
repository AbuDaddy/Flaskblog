from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
