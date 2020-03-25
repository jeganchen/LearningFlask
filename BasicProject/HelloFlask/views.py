from flask import Flask, render_template
from HelloFlask import app
from datetime import datetime


@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    format_date = now.strftime("%A, %d %B, %Y at %X")
    title = "Hello Flask"
    message = "Hello Flask!"
    content = "on " + format_date
    return render_template("index.html", title=title, message=message, content=content)

@app.route('/about')
def about():
    return render_template("about.html",
                           title='About Flask',
                           content='all about flask')
