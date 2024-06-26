from flask import Flask, render_template
import time
from emp import empy_data
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    return render_template("about.html",title='about')

@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html",
                           title="evaluate",
                           number=num)

@app.route("/emp")
def emp():
     return render_template("emp.html",
                           title="employee",
                           emp=empy_data
                           )
@app.route("/mgr")
def mgr():
     return render_template("mgr.html",
                           title="Manager",
                           emp=empy_data
                           )



if __name__ == '__main__':
    app.run(debug=True)
