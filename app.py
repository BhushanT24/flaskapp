# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
app.secret_key = "aaaaa"
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       return "Your name is "+first_name + last_name
    return render_template("index.html")
 
if __name__=='__app__':
   app.run()
