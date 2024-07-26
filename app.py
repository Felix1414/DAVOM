from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Configura tu clave API directamente aquí
openai.api_key = 'sk-proj-7JQ0XqwiR3X2S726OkvQT3BlbkFJSJzSklT1XDwtBDZtsFlo'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    try:
        pregunta = request.form['pregunta']
        respuesta = obtener_respuesta_openai(pregunta)
        return render_template('resultado.html', respuesta=respuesta)
    except Exception as e:
        # Manejo de errores
        print(f"Error: {e}")
        return render_template('resultado.html', respuesta="Ocurrió un error al procesar la solicitud.")

def obtener_respuesta_openai(pregunta):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": pregunta}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        # Manejo de errores
        print(f"Error en OpenAI API: {e}")
        return "Ocurrió un error al obtener la respuesta."

if __name__ == '__main__':
    app.run(debug=True)
