from flask import Flask, redirect, render_template, request
# template de HTML, verbos HTTP, troca de URL
from Viga import Viga
import comandos_mongodb

app = Flask(__name__)
app.config["SECRET_KEY"] = "Frankenstein"

@app.route('/inicio', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        global obj_viga
        carga = float(request.form["input_carga"])
        comprimento = float(request.form["input_comprimento"])
        base = float(request.form["input_base"])
        altura = float(request.form["input_altura"])
        resistencia = float(request.form["input_resistencia"])
        obj_viga = Viga(carga, comprimento, base, altura, resistencia)
        comandos_mongodb.adicionar_viga(obj_viga.carga, obj_viga.comprimento, obj_viga.base, obj_viga.altura, obj_viga.resistencia)
        # texto = comandos_mongodb.mostrar_dados_viga(comandos_mongodb.id_viga)
        comandos_mongodb.id_viga += 1
        # global resultado
        return redirect("/resultado")
    return render_template('index.html')

@app.route("/resultado", methods=["GET", "POST"])
def mostrar_resultados():
    if request.method == "POST":
        return redirect("/inicio")
    else:
        dados_entrada = comandos_mongodb.mostrar_dict_viga(1) # problemas com id
        carga = dados_entrada["carga"]
        comprimento = dados_entrada["comprimento"]
        base = dados_entrada["base"]
        altura = dados_entrada["altura"]
        resistencia = dados_entrada["resistencia_material"]
        obj_viga = Viga(carga, comprimento, base, altura, resistencia)
        resultado = obj_viga.verificar_tensao_viga()
        dados_formatados = comandos_mongodb.mostrar_dados_viga(1)
        return render_template("saida_dados.html", dados_entrada=dados_formatados, resultado=resultado)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
