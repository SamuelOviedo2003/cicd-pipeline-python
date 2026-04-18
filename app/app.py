"""
This module provides methods to connect the app
"""

# app/app.py
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False


@app.route("/", methods=["GET"])
def index():
    """Carga el formulario principal."""
    return render_template("index.html", resultado=None)


@app.route("/", methods=["POST"])
def calcular():
    """This function provides methods to connect the user with the app"""
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(port=5000, host="127.0.0.1")
