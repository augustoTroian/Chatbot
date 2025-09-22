import argparse
from transformers import pipeline

def iniciar_chat(modo):
    if modo == "curto":
        generator = pipeline("text-generation", model="distilgpt2")
        print("🤖 Chatbot LLM (modo CURTO) iniciado!")
    else:
        generator = pipeline("text-generation", model="gpt2")
        print("🤖 Chatbot LLM (modo CRIATIVO) iniciado!")

    print("Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Bot: Até logo!")
            break
        resposta = generator(user_input, max_length=50 if modo=="curto" else 150, num_return_sequences=1)[0]['generated_text']
        print("Bot:", resposta)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--modo", choices=["curto", "criativo"], default="curto", help="Escolha o modo de resposta")
    args = parser.parse_args()
    iniciar_chat(args.modo)
