import os
import sqlite3
from flask import Flask, request, jsonify
from utils import buscar_respuesta_local
from openai import OpenAI

# Configuración de la API Key de OpenAI
#openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

app = Flask(__name__)

# Crear la tabla de conversaciones si no existe
def init_db():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS conversations (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_input TEXT NOT NULL,
                      bot_response TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Llamar a la función para inicializar la base de datos
init_db()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("input")
    
    
    # Buscar en el historial de respuestas locales
    respuesta_local, efectividad = buscar_respuesta_local(user_input)
    model="gpt-4",
    if respuesta_local:
        return jsonify({"response": respuesta_local, "confidence": efectividad, "source": "local"})
    
    # Si no se encuentra respuesta local satisfactoria, usar OpenAI
    #response = openai.ChatCompletion.create(
    #    model="gpt-4",
    #    messages=[{"role": "user", "content": user_input}],
    #    max_tokens=100,
    #    temperature=0.7
    #)
    #answer = response.choices[0].message['content'].strip()
    response = client.chat.completions.create(
        model="gpt-4o",
#        prompt = user_input,
        messages=[{"role": "user", "content": user_input}],
        max_tokens=100,
        temperature=0.7
#        top_p=1.0,
#        frequency_penalty=0.0,
#        presence_penalty=0.0,
#        stop=["\n", "Human:", "AI:"]
        
    )
    print("*********************************************")
    print(response.choices[0].message.content)
    print("*********************************************")
    answer = response.choices[0].message.content

    # Guardar la conversación en la base de datos local
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO conversations (user_input, bot_response) VALUES (?, ?)", (user_input, answer))
    conn.commit()
    conn.close()

    return jsonify({"response": answer, "confidence": "from API", "source": "openai"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
