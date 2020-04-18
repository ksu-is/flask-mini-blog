from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/home')
def index():
   return render_template('home.html')


@app.route('/travel')
def travel():
    return render_template('travel.html')


if __name__ == "__main__":
    app.run(debug = True)