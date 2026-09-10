import requests

WEBHOOK_URL = "https://hook.us2.make.com/4ru188mnidz7xxydnmyvhtvhvpqvtx77"
             
def enviar_sinal(texto_sinal):
    payload = {
        "mensagem": texto_sinal
    }
    
    try:
        resposta = requests.post(WEBHOOK_URL, json=payload)
        if resposta.status_code == 200:
            print("[SUCESSO] Sinal enviado para o Make e Telegram!")
        else:
            print(f"[ERRO] Falha ao enviar: {resposta.status_code}")
    except Exception as e:
        print(f"[ERRO DE CONEXÃO]: {e}")

if __name__ == "__main__":
    sinal_exemplo = "🚨 *SINAL AVIATOR* 🚨\nEntrada confirmada em 2.00x!"
    enviar_sinal(sinal_exemplo)
