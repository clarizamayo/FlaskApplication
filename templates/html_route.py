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

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return result
    else:
        return f"this was a {request.method}"
    
