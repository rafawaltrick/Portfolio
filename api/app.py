
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/projecao")
def projecao():
    return render_template("projecao.html")
@app.route("/")    
@app.route("/sobremim")
def sobremim():
    return render_template("sobremim.html")
@app.route("/curriculo")
def curriculo():
    return render_template("teste.html")    


if __name__=="__main__":
    app.run(debug=True)