from flask import Flask,make_response,request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    response=make_response("<h1>Welcome to HHome PAge</h1>")
    return response
@app.route("/set_cookie")
def set_cookie():
   response=make_response("<h1>Welcome to HHome PAge</h1>")
   response.set_cookie("Cookie_name","Cookie_value")
   return response

@app.route("/get_cookie")
def get_cookie():
   value= request.cookies.get("Cookie_name")
   response=make_response(f"<h1>The Cookie Value is <i>{value}</i></h1>")
   return response

if __name__== "__main__":
  app.run(debug=True)