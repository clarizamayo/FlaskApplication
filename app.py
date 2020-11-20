from flask import Flask, render_template,request, url_for
from flask_sqlalchemy import SQLAlchemy
import math
from tasks import covid_data
url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

app = Flask(__name__)
app.config['SECRET_KEY'] = "402d6cadba1d4c9cb5eca4d58faaf1ec"

@app.route('/')
def welcome_msg():
    return f"The following table is being scraped from {url}"

@app.route('/coviddata')
def covid_table():
    table = covid_data(url)
    return render_template("table.html", data=table)

@app.route('/contact', methods=["GET", "POST"])
def register():
    return render_template("contact.html")
    
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        attempted_username = request.form['username']
        attempted_password = request.form['password']
        return f"this was a {request.method}, username: {attempted_username}, password: {attempted_password}"
    else:
        return f"this was a {request.method}"

if __name__ == '__main__':
    app.run(debug=True)