from flask import Flask, render_template
app = Flask(__name__,template_folder='templates')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/recetas")
def hello():
    return render_template("recetas.html")

if __name__ == "__main__":
    app.run(debug=True)
