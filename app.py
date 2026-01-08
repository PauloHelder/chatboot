import requests
from flask import Flask, request, jsonify

#from services.waha import Waha
BASE_URL = 'https://diligent-abundance-production.up.railway.app'
#BASE_URL = 'https://evolution-api-production-e345.up.railway.app'
INSTANCE_NAME = 'kdigital'
EVOLUTION_AUTHENTICATION_API_KEY = 'Php.123#321@'

headers = {
    'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
    'Content-Type': 'application/json'
}


app = Flask(__name__)


@app.route('/chatbot/webhook', methods=['GET'])
def getall():
    return jsonify({'status': 'success'}), 200

@app.route('/chatbot/webhook/messages-upsert', methods=['POST'])
def webhook():
    data = request.json

    #number = data['data']['pushName']
    number = '244973967181'
    print(f'EVENTO RECEBIDO: {data}')

   # waha = Waha()

   #chat_id = data['payload']['from']
   #waha.send_message(
   #    chat_id=chat_id,
   #  message='Resposta Automática :)', )

    payload = {
    'number': number,
    'text': 'KomunhãoDigital!',
    # 'delay': 10000, # simular "digitando"
}
    response = request.post(
    url=f'{BASE_URL}/message/sendText/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)
    print(response.json())


    

    return jsonify({'status': 'success'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


























