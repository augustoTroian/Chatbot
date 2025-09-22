# Projeto - Comparação entre Chatbots Antigos e Atuais

Este projeto apresenta 3 chatbots diferentes, seguindo os requisitos da atividade:

1. **FAQ Chatbot (`faq_chatbot.py`)**
   - Chatbot em português com base de conhecimento >50 perguntas/respostas.

2. **Rule-based Chatbot (`rule_chatbot.py`)**
   - Chatbot simples baseado em regras de if/else.

3. **LLM Chatbot (`llm_chatbot.py`)**
   - Chatbot com modelo de linguagem treinado.
   - Dois modos de resposta: curto (mais objetivo) e criativo (mais aberto).

---

## Dependências

Antes de rodar os chatbots, instale as bibliotecas necessárias.

### Passo 1 – Atualizar instalador
```bash
python -m pip install --upgrade pip setuptools wheel
```

### Passo 2 – Instalar dependências principais (um de cada vez)
```bash
pip install transformers
pip install torch
```

### Passo 3 - colocar (cd + o caminho para a pasta com os arquivos)

Observação: se você estiver usando **Python 3.13**, pode ter problemas ao rodar `pip install -r requirements.txt`.  
Nesse caso, siga os comandos acima manualmente.

---

## Como executar

### FAQ Chatbot
```bash
python faq_chatbot.py
```

### Chatbot baseado em regras
```bash
python rule_chatbot.py
```

### LLM Chatbot
- Modo curto:
```bash
python llm_chatbot.py --modo curto
```
- Modo criativo:
```bash
python llm_chatbot.py --modo criativo
```

---

## Observação
Capturas de tela de execução devem ser incluídas no relatório final.
