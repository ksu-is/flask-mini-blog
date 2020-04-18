from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/home')
def index():
   return render_template('home.html')


@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == "__main__":
    app.run(debug = True)