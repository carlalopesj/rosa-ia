import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai
import textwrap

app = Flask(__name__)

# Pegando a chave da API Gemini da variável de ambiente
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Função para enviar a mensagem via API Gemini
def enviar_mensagem_gemini(mensagem):
    model = genai.GenerativeModel("gemini-1.5-flash")
    resposta = model.generate_content(mensagem)
    return resposta.text  # Retorna apenas o texto

# Função para dividir o texto em blocos menores
def dividir_em_blocos(texto, largura=1600):
    return textwrap.wrap(texto, width=largura)

# Endpoint para receber mensagens via Twilio
@app.route('/mensagem', methods=['POST'])
def mensagem():
    incoming_msg = request.values.get('Body', '').strip()
    resposta = MessagingResponse()

    print(f"Mensagem recebida: {incoming_msg}")  # Log da mensagem recebida

    # Gera resposta via Gemini AI
    try:
        gemini_resposta = enviar_mensagem_gemini(incoming_msg)
        print(f"Resposta do Gemini: {gemini_resposta}")  # Log da resposta gerada

        if gemini_resposta:  # Verifica se a resposta não está vazia
            blocos = dividir_em_blocos(gemini_resposta)  # Divide a resposta em blocos
            for bloco in blocos:
                resposta.message(bloco)  # Enviar cada bloco como uma mensagem separada
        else:
            resposta.message("Desculpe, a resposta do Gemini está vazia.")
    except Exception as e:
        print(f"Erro ao chamar a API Gemini: {e}")
        resposta.message("Desculpe, houve um erro ao processar sua mensagem.")

    return str(resposta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
