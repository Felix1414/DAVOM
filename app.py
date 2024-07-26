import openai
from flask import Flask, request, render_template

app = Flask(__name__)

# Configura tu clave API de OpenAI
openai.api_key = 'sk-proj-7JQ0XqwiR3X2S726OkvQT3BlbkFJSJzSklT1XDwtBDZtsFlo'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    pregunta = request.form['pregunta']
    
    # Llamada a la API de OpenAI usando el modelo de chat
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # O el modelo que prefieras
        messages=[
            {"role": "user", "content": pregunta}
        ],
        max_tokens=150
    )
    
    respuesta = response.choices[0].message['content'].strip()
    return render_template('resultado.html', respuesta=respuesta)

if __name__ == '__main__':
    app.run(debug=True)
