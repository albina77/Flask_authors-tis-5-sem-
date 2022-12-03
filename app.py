from flask import Flask, render_template
from db_lib import WorksData
import sqlite3

wd = WorksData()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/persons')
def persons():
    persons_list = wd.get_persons()
    return render_template('Persons.html', persons_list=persons_list)

@app.route('/persons/<person_id>')
def person_details(person_id=None):
    person_name = wd.get_author_name(person_id)
    countries = wd.get_countries(person_id)
    works = wd.get_works(person_id)
    ret = render_template("Person_details.html", person=person_name, Countries=countries, works=works)
    return ret

@app.route('/works')
def works():
    works_list = wd.get_work()
    types = wd.get_types()
    return render_template('Works.html', works_list=works_list, types = types)

@app.route('/works/<work_id>')
def work_details(work_id=None):
    work_name = wd.get_work_name(work_id)
    countries = wd.get_countries_works(work_id)
    authors = wd.get_authors(work_id)
    ret = render_template("Work_details.html", work=work_name, Countries=countries, authors=authors)
    return ret

if __name__ == "__main__":
    app.run(debug=True)