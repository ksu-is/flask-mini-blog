import datetime
from flask import Flask, render_template, request
import database


app = Flask(__name__)
##entries = []

database.create_tables()

@app.route('/')
def index():
   return render_template('home.html')


@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/forms', methods=["GET", "POST"])
def forms():
    if request.method == "POST":
        entry_content = request.form.get("content")
        ##content will be associated with textarea
        database.create_entry(entry_content, datetime.datetime.today().strftime("%b %d"))
        
     ##Gets user back to form page so that they can type more   
    return render_template("forms.html", entries=database.retrieve_entries())
    
if __name__ == "__main__":
    app.run(debug = True)
    