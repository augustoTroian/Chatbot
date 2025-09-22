# Chatbot FAQ em português com mais de 50 pares de perguntas e respostas

def faq_bot():
    faq = {
        "olá": "Olá! Como posso te ajudar?",
        "oi": "Oi! Tudo bem? Como posso ajudar?",
        "qual seu nome?": "Eu sou um chatbot de exemplo para FAQs.",
        "quem é você?": "Sou um bot criado para responder perguntas frequentes.",
        "como você funciona?": "Eu tenho uma base de perguntas e respostas pré-definidas.",
        "o que é ia?": "IA significa Inteligência Artificial, a simulação de processos humanos por máquinas.",
        "o que é machine learning?": "Machine Learning é uma área da IA que ensina máquinas a aprender com dados.",
        "o que é python?": "Python é uma linguagem de programação popular e fácil de aprender.",
        "me fale sobre chatbots": "Chatbots são programas que simulam conversas humanas.",
        "quem criou você?": "Fui criado por um estudante como parte de um trabalho acadêmico.",
        "adeus": "Até mais! Foi bom conversar com você.",
        "tchau": "Tchau! Volte sempre.",
        "obrigado": "De nada! Estou aqui para ajudar.",
        "valeu": "Disponha! 😉",
        "como está o clima?": "Não sei exatamente, mas você pode verificar em um site de clima.",
        "qual a capital do brasil?": "A capital do Brasil é Brasília.",
        "quem descobriu o brasil?": "O Brasil foi descoberto em 1500 por Pedro Álvares Cabral.",
        "quantos estados tem o brasil?": "O Brasil possui 26 estados e 1 distrito federal.",
        "quem é o presidente do brasil?": "O presidente atual pode variar, verifique em fontes confiáveis.",
        "me fale uma curiosidade": "Você sabia que o polvo tem três corações?",
        "me conte uma piada": "Por que o livro de matemática ficou triste? Porque tinha muitos problemas!",
        "qual a sua função?": "Minha função é responder perguntas frequentes em português.",
        "você fala inglês?": "Sim, mas este chatbot foi treinado em português.",
        "qual sua idade?": "Eu não tenho idade, sou apenas um programa.",
        "você gosta de música?": "Se eu pudesse, ouviria bastante música!",
        "me recomende um filme": "Um clássico é 'O Senhor dos Anéis'.",
        "me recomende uma série": "Que tal 'Stranger Things'?",
        "me recomende um livro": "Sugiro '1984' de George Orwell.",
        "qual sua comida favorita?": "Se eu comesse, acho que adoraria pizza 🍕.",
        "qual a linguagem mais usada?": "Python, JavaScript e Java estão entre as mais usadas atualmente.",
        "o que é github?": "GitHub é uma plataforma para hospedar e compartilhar códigos.",
        "o que é algoritmo?": "Um algoritmo é uma sequência de passos para resolver um problema.",
        "me explique nuvem": "Nuvem é o armazenamento e processamento de dados em servidores online.",
        "como estudar ia?": "Você pode começar com Python, depois aprender machine learning e deep learning.",
        "onde fica a frança?": "A França está localizada na Europa.",
        "qual a capital da frança?": "A capital da França é Paris.",
        "me fale sobre paris": "Paris é conhecida como a Cidade Luz e famosa pela Torre Eiffel.",
        "o que é internet?": "A internet é uma rede mundial que conecta computadores.",
        "quem inventou a luz elétrica?": "Thomas Edison é creditado pela invenção da lâmpada elétrica.",
        "quem foi einstein?": "Einstein foi um físico famoso pela teoria da relatividade.",
        "o que é cpu?": "CPU é a Unidade Central de Processamento, o 'cérebro' do computador.",
        "o que é gpu?": "GPU é a unidade de processamento gráfico, ótima para IA e jogos.",
        "qual o melhor sistema operacional?": "Isso depende, Windows, Linux e macOS têm vantagens diferentes.",
        "como você aprende?": "Eu não aprendo, apenas uso respostas pré-definidas.",
        "qual sua linguagem nativa?": "Fui escrito em Python.",
        "você gosta de humanos?": "Claro, fui criado para conversar com humanos!",
        "qual a cor do céu?": "Durante o dia geralmente é azul, à noite escuro com estrelas.",
        "quem foi newton?": "Isaac Newton foi um cientista que formulou as leis do movimento e da gravidade.",
        "quem inventou o avião?": "Os irmãos Wright são considerados os inventores do avião.",
        "qual o maior animal do mundo?": "A baleia-azul é o maior animal conhecido.",
        "me fale uma frase motivacional": "O sucesso é a soma de pequenos esforços repetidos diariamente."
    }

    print("Chatbot FAQ iniciado! Digite 'sair' para encerrar.")
    while True:
        pergunta = input("Você: ").lower()
        if pergunta == "sair":
            print("Bot: Até logo!")
            break
        resposta = faq.get(pergunta, "Desculpe, não entendi sua pergunta.")
        print("Bot:", resposta)


if __name__ == "__main__":
    faq_bot()
