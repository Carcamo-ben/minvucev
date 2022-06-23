from flask import Flask, render_template, url_for,request
app = Flask(__name__,template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recetas")
def recetas():
    return render_template("recetas.html")

@app.route('/handle_form>', methods = ['GET', 'POST', 'DELETE'])
def handle_form():
    data= request.form
    print (data['comuna'])
    print (data['latitud'])
    request.post("https://prod-25.eastus.logic.azure.com:443/workflows/82bb213964e7477e97c1b949fe51544f/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=bDydfFCFFrBmgCF1qHpjCGIMVoKI_5CcmCSV1n2v5kw",data))
    return data