from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/second')
def second_page():
    return 'This is my second page'

@app.route('/about-me')
def about_me():
    return 'This is aboutme page'

if __name__ == "__main__":
    app.run()