from flask import Flask, render_template, url_for
app = Flask(__name__,template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recetas")
def recetas():
    return render_template("recetas.html")

