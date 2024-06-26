from flask import Flask,flash,redirect, render_template,url_for
from form import Signupform, loginform
app = Flask(__name__)
app.config["SECRET_KEY"]="test_test"
@app.route("/")
def home():
  return  render_template("home.html",title='Home')

@app.route("/signin",methods=['GET','POST'])
def signin():
  form = Signupform()
  if form.validate_on_submit():
    flash(f"Sign up Successful {form.username.data}!")
    return redirect(url_for("home"))
  return render_template("signin.html", title="Sign in",form= form)

@app.route("/login",methods=['GET','POST'])
def login():
  form = loginform()
  if form.validate_on_submit():
    email= form.email.data
    pw= form.Password.data
    if email=="amit@gmail.com" and pw=="12345":
      flash(f"Login up Successful {form.email.data}!")
      return redirect(url_for("home"))
    else:
      flash(f"Incorrect Login credentials!")
  return render_template("login.html", title="login",form=form)


if __name__ == '__main__':
  app.run(debug=True)
