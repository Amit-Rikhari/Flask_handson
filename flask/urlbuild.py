from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to home page</h1>"

@app.route("/passed/<sname>/<int:num>")
def passed(sname,num):
    return f"<h1>Congrats {sname.title()} you have passed your marks is {num}</h1>"

@app.route("/failed/<sname>/<int:num>")
def failed(sname,num):
    return f"<h1>Sorry {sname.title()} you have failed and  your marks is {num}</h1>"

@app.route("/score/<name>/<int:marks>")
def score(name, marks):
    if marks < 30:
        time.sleep(2)
        # Redirect to failed route using url_for
        return redirect(url_for('failed',sname=name,num=marks))
    else:
        time.sleep(2)
        # Redirect to passed route using url_for
        return redirect(url_for('passed',sname=name,num=marks))

if __name__ == '__main__':
    app.run(debug=True)
