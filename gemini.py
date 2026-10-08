# Este arquivo cuida somente da comunicação com a API Gemini.

# Importa a biblioteca oficial do Google para conversar com a API Gemini
from google import genai
# Importa o módulo "os" para ler variáveis de ambiente (onde fica a chave da API)
import os
# Importa a função que lê o arquivo .env e transforma suas linhas em variáveis de ambiente
from dotenv import load_dotenv

# Carrega o arquivo .env (onde está GEMINI_API_KEY) para que o os.environ consiga enxergá-la
load_dotenv()

# Define o nome do modelo do Gemini que será usado nas análises
MODELO = "gemini-2.5-flash"


# Função que envia o prompt ao Gemini e devolve o texto da resposta
def consultar_gemini(prompt):
    # Lê a chave da API da variável de ambiente GEMINI_API_KEY (assim ela não fica escrita no código)
    chave = os.environ.get("GEMINI_API_KEY")
    # Se a chave não existir, avisa o usuário em vez de dar erro
    if not chave:
        # Devolve a mensagem de aviso e encerra a função
        return "Erro: a variável de ambiente GEMINI_API_KEY não foi configurada."
    # Tenta chamar a API; o try evita que a página quebre se algo der errado
    try:
        # Cria o cliente do Gemini usando a chave
        cliente = genai.Client(api_key=chave)
        # Envia o prompt ao modelo escolhido e guarda a resposta
        resposta = cliente.models.generate_content(model=MODELO, contents=prompt)
        # Devolve apenas o texto gerado pela IA
        return resposta.text
    # Se qualquer erro acontecer (internet, chave inválida etc.), cai aqui
    except Exception as erro:
        # Devolve uma mensagem de erro amigável com o motivo
        return f"Erro ao consultar o Gemini: {erro}"
