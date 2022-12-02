from flask import Flask, redirect, render_template, request
# template de HTML, verbos HTTP, troca de URL
from Viga import Viga
import comandos_mongodb

app = Flask(__name__)
app.config["SECRET_KEY"] = "Frankenstein"

# texto = ""
resultado = ""

@app.route('/inicio', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        carga = float(request.form["input_carga"])
        comprimento = float(request.form["input_comprimento"])
        base = float(request.form["input_base"])
        altura = float(request.form["input_altura"])
        resistencia = float(request.form["input_resistencia"])
        obj_viga = Viga(carga, comprimento, base, altura, resistencia)
        comandos_mongodb.adicionar_viga(carga, comprimento, base, altura, resistencia)
        # global texto
        texto = comandos_mongodb.mostrar_dados_viga(comandos_mongodb.id_viga)
        comandos_mongodb.id_viga += 1
        global resultado
        resultado = obj_viga.verificar_tensao_viga()
        return redirect("/resultado")
    return render_template('index.html')

@app.route("/resultado", methods=["GET", "POST"])
def mostrar_resultados():
    if request.method == "POST":
        return redirect("/inicio")
    else:
        return render_template("saida_dados.html")
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
