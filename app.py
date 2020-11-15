from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask('webapp')

URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_percentage_of_population_living_in_poverty'
page = requests.get(URL)

soup = BeautifulSoup(page.content)

@app.route('/')
def home():
    return soup.prettify()

@app.route('/user/<username>')
def message(username):
    return f"Hello {username}. Nice to meet you!"

import math
@app.route('/sqrt/<num>')
def squared_root_num(num):
    return str(math.sqrt(int(num)))

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return result
    else:
        return f"this was a {request.method}"

if __name__ == '__main__':
    app.run(debug=True)