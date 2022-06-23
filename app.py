from flask import Flask, render_template, url_for,request
app = Flask(__name__,template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recetas")
def recetas():
    return render_template("recetas.html")

@app.route('/handle_form>', methods = ['GET', 'POST', 'DELETE'])
def handle_form:
    data= request.form
    print (data['comuna'])
    print (data['latitud'])
    return data