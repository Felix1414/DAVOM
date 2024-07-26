from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Configura tu clave API
openai.api_key = 'sk-proj-tV2O0ZBsOb33boFbuGZ5T3BlbkFJdz0w8mtUyEqzMdPhc8wb'

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

