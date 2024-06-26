from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to home page</h1>"

@app.route("/passed")
def passed():
    return "<h1>Congrats you have passed</h1>"

@app.route("/failed")
def failed():
    return "<h1>you have failed Sorry:</h1>"

@app.route("/score/<name>/<int:marks>")
def score(name, marks):
    if marks < 30:
        time.sleep(0)
        # Redirect to failed route using url_for
        return redirect(url_for('failed'))
    else:
        time.sleep(0)
        # Redirect to passed route using url_for
        return redirect(url_for('passed'))

if __name__ == '__main__':
    app.run(debug=True)
