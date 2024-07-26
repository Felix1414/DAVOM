import openai
from flask import Flask, request, render_template

app = Flask(__name__)

# Configura tu clave API de OpenAI
openai.api_key = 'tu_clave_api'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    pregunta = request.form['pregunta']
    
    # Llamada a la API de OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",  # Puedes elegir el modelo que prefieras
        prompt=pregunta,
        max_tokens=150
    )
    
    respuesta = response.choices[0].text.strip()
    return render_template('resultado.html', respuesta=respuesta)

if __name__ == '__main__':
    app.run(debug=True)
