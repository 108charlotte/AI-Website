from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tutorials')
def tutorials(): 
    return render_template("tutorials.html")

@app.route('/aboutme')
def aboutme(): 
    return render_template("error.html", error=404) 

@app.route('/welcome')
def welcome(): 
    return "It works!"

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)