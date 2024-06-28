from flask import Flask

app= Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome Home</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Welcome {name} to the page </h1>"


@app.route("/addition/<int:num>")
def addition(num):
    return f"<h1>Add number{num+10}</h1>"

@app.route("/addition_two/<int:num>/<int:n>")
def addition_two(num,n):
    return f"<h1>2 number{num+n}</h1>"

@app.route("/about")
def about():
    return "<h1>About Me!</h1>"
if __name__ == '__main__':
    app.run(debug=True)
