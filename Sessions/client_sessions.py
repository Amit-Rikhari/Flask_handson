from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash,
    session,
    request
                   )

from form import loginform

app= Flask(__name__)

app.config ['SECRET_KEY']='sec'

@app.route("/")

@app.route("/home")
def home():
   return render_template("home.html",title="Home")

@app.route("/login", methods=['GET', 'POST'])
def login():
   form=loginform()
   if form.validate_on_submit():
      session['user_name']=form.username.data
      flash(f"Login Successful {session['user_name']}")
      next_url= request.args.get(next)
      return redirect(next_url or url_for('home'))
   else:
        flash("Invalid")
   return render_template("login.html",title="Login",form=form)
  
@app.route("/about")
def about():
   if "user_name" not in session:
      # flash("Login required")
      return redirect(url_for('login',next=request.url))
   else:
      flash(f"Hi {session['user_name']},Have a Good Day")
   return render_template("about.html",title="About")

@app.route("/contact")
def contact():
   if "user_name" not in session:
      flash("Login required")
      return redirect(url_for('login',next=request.url))
   else:
      flash(f"Hi {session['user_name']},Have a Good Day")
 
   return render_template("contact.html",title="Contact")

if __name__=="__main__":
   app.run(debug=True)

