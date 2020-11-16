from flask import Flask, render_template,request
import math
from tasks import covid_data

app = Flask(__name__)

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

@app.route('/')
def welcome_msg():
    return f"The following table is being scrapped from {url}"

@app.route('/covid')
def covid_table():
    table = covid_data(url)
    return render_template("table.html", data=table)

@app.route('/user/<username>')
def message(username):
    return f"Hello {username}. Nice to meet you!"

@app.route('/sqrt/<num>')
def squared_root_num(num):
    return str(math.sqrt(int(num)))

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        attempted_username = request.form['username']
        attempted_password = request.form['password']
    else:
        return f"this was a {request.method}"

if __name__ == '__main__':
    app.run(debug=True)