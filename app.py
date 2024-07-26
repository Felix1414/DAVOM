from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    pregunta = request.form['pregunta']
    # Aquí iría la lógica para manejar la consulta
    respuesta = 'Respuesta a la pregunta'  # Sustituir con lógica real
    return render_template('resultado.html', respuesta=respuesta)

if __name__ == '__main__':
    app.run(debug=True)
#########################################################################
fallas_soluciones = {
    "ruido excesivo": "Verifica la alineación de los rodillos.",
    "fallo en el enrollador": "Revisa el sistema de frenos.",
    # Agrega más fallas y soluciones aquí
}

@app.route('/consultar', methods=['POST'])
def consultar():
    pregunta = request.form['pregunta'].lower()
    respuesta = fallas_soluciones.get(pregunta, "No se encontró una solución para el problema.")
    return render_template('resultado.html', respuesta=respuesta)
