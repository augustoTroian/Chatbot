# Chatbot baseado em regras simples

def rule_chatbot():
    print("Chatbot Regras iniciado! Digite 'sair' para encerrar.")
    while True:
        user = input("Você: ").lower()
        if user == "sair":
            print("Bot: Tchau!")
            break
        elif "oi" in user or "olá" in user:
            print("Bot: Oi, tudo bem?")
        elif "como você está" in user:
            print("Bot: Estou sempre bem, obrigado por perguntar!")
        elif "qual seu nome" in user:
            print("Bot: Eu sou um chatbot baseado em regras.")
        else:
            print("Bot: Não entendi, pode reformular?")

if __name__ == "__main__":
    rule_chatbot()
