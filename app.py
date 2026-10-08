# Importa a classe Flask (cria o app), render_template (mostra o HTML) e request (lê o formulário enviado)
from flask import Flask, render_template, request
# Importa dos prompts.py os dois textos de instrução para a IA
from prompts import PROMPT_EXPLICAR, PROMPT_ERROS
# Importa do gemini.py a função que conversa com a API Gemini
from gemini import consultar_gemini
# Importa o conversor que transforma o texto Markdown da IA (**negrito**, ```código```) em HTML
from markdown_it import MarkdownIt

# Cria a aplicação Flask; __name__ diz ao Flask onde estão as pastas "templates" e "static"
app = Flask(__name__)

# Define o limite máximo de caracteres que o código colado pode ter
LIMITE = 3000

# Cria o conversor; "html": False impede que tags HTML escritas pela IA sejam executadas (segurança)
conversor = MarkdownIt("commonmark", {"html": False})


# Função que recebe o texto cru da IA e devolve o HTML já formatado
def deixar_bonito(texto):
    # Converte o Markdown em HTML (títulos, negrito, listas, blocos de código...)
    return conversor.render(texto)


# Define a rota principal "/", aceitando abrir a página (GET) e enviar o formulário (POST)
@app.route("/", methods=["GET", "POST"])
def inicio():
    # Começa com o código vazio (usado para manter o texto no campo após enviar)
    codigo = ""
    # Começa com a opção "explicar" marcada
    acao = "explicar"
    # Começa sem resposta da IA (já formatada em HTML)
    resposta_bonita = ""
    # Começa sem mensagem de erro de validação
    erro = ""

    # Só entra aqui se o usuário clicou em "Analisar" (formulário enviado)
    if request.method == "POST":
        # Lê o código digitado e remove espaços extras no começo e no fim
        codigo = request.form.get("codigo", "").strip()
        # Lê qual opção foi escolhida; se não vier nada, usa "explicar"
        acao = request.form.get("acao", "explicar")

        # Validação 1: o campo não pode estar vazio
        if not codigo:
            # Define a mensagem que será mostrada ao usuário
            erro = "Por favor, cole um código antes de analisar."
        # Validação 2: o código não pode passar do limite de caracteres
        elif len(codigo) > LIMITE:
            # Define a mensagem informando o tamanho enviado e o limite
            erro = f"O código tem {len(codigo)} caracteres. O limite é {LIMITE}."
        # Se o código é válido, chama a IA
        else:
            # Escolhe o prompt de acordo com a opção marcada
            prompt = PROMPT_ERROS if acao == "erros" else PROMPT_EXPLICAR
            # Junta o prompt com o código e envia ao Gemini (função do gemini.py)
            resposta = consultar_gemini(prompt + codigo)
            # Formata a resposta da IA para ficar bonita na tela
            resposta_bonita = deixar_bonito(resposta)

    # Mostra a página HTML, enviando as variáveis para o template usar
    return render_template("index.html", codigo=codigo, acao=acao, resposta_bonita=resposta_bonita, erro=erro, limite=LIMITE)


# Executa somente se este arquivo for rodado diretamente (python app.py)
if __name__ == "__main__":
    # Inicia o servidor local de desenvolvimento em http://127.0.0.1:5000
    app.run(debug=True)
