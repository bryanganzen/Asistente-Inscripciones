from openai import OpenAI
import re
import time
from flask import Flask, request, jsonify
import os
from datetime import datetime
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Ruta para acceder a las credenciales de BigQuery"

schema = [
    bigquery.SchemaField("datetime", "TIMESTAMP"),
    bigquery.SchemaField("question", "STRING"),
    bigquery.SchemaField("answer", "STRING")
]

app = Flask(__name__)
client = OpenAI(api_key="tu_clave_api")
bigquery_client = bigquery.Client()

def create_new_thread():
    """Crea un nuevo hilo en la API de OpenAI y devuelve su ID."""
    thread = client.beta.threads.create()
    thread_id = thread.id
    return thread_id

def limpiar_referencias(texto):
    """Elimina referencias ilegibles del texto."""
    patron_referencias = r'【[^】]*\.pdf】|【[^\】]*†[^\】]*】'
    texto_limpio = re.sub(patron_referencias, '', texto)
    return texto_limpio

def get_assistant_response(user_message, thread_id):
    """Envía un mensaje del usuario al asistente de OpenAI y devuelve la respuesta."""
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id="id_asistente_aqui"
    )

    while True:
        time.sleep(5)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=thread_id
            )
            answer = limpiar_referencias(messages.data[0].content[0].text.value)

            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            question = user_message
            table_id = 'id_tabla_de_BigQuery_aqui'
            rows_to_insert = [(current_datetime, question, answer)]
            bigquery_client.insert_rows(table_id, rows_to_insert, selected_fields=schema)

            return answer

@app.route('/conversation', methods=['POST'])
def conversation():
    """Maneja las solicitudes POST para iniciar una conversación con el asistente."""
    user_message = request.json['message']
    thread_id = create_new_thread()
    response = get_assistant_response(user_message, thread_id)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)