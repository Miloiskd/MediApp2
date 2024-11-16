from flask import Flask, render_template, request, redirect, url_for
from functions.SaludBiologica import SaludBiologica

app = Flask(__name__)

@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        altura = float(request.form["altura"])
        peso = float(request.form["peso"])
        edad = int(request.form["edad"])
        sexo = request.form["sexo"]
        frecuencia_cardiaca = int(request.form["frecuencia_cardiaca"])
        salud = SaludBiologica(altura, peso, edad, sexo, frecuencia_cardiaca)
        
        datos = {
            "IMC": salud.calcular_IMC(),
            "Interpretación IMC": salud.interpretar_IMC(),
            "Tasa Metabólica Basal": salud.CalcularTasaMeta(),
            "Datos Completos": salud.mostrar_datos()
        }

        return render_template("resultados.html", datos=datos)
    return render_template("formulario.html")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
