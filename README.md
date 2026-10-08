# Ponto & Vírgula

Esqueceu o ponto e vírgula? A gente te ajuda!

O Ponto & Vírgula é um site simples onde você cola um código e uma IA explica ele ou acha os erros. Funciona com qualquer linguagem que o Gemini reconheça, tipo Python, C, Java, JavaScript, PHP, SQL, HTML e CSS. Não precisa escolher a linguagem, a própria IA descobre sozinha.

## Como usar

1. Cola o código no campo de texto (até 3000 caracteres)
2. Escolhe entre "Explicar código" ou "Identificar erros"
3. Clica em "Analisar"
4. Lê a resposta

A IA só lê o código, ela não executa nem compila nada.

## Tecnologias

- HTML5 e CSS3
- Python com Flask
- API Gemini

Sem JavaScript no frontend e sem banco de dados, a ideia era fazer o mais simples possível.

## Arquivos

- `app.py`: rotas do Flask, formulário e validações
- `gemini.py`: conversa com a API do Gemini
- `prompts.py`: os textos de instrução que a gente manda pra IA
- `templates/index.html`: a página
- `static/style.css`: o visual

## Como rodar

Instala as bibliotecas:

```
pip install -r requirements.txt
```

Cria um arquivo `.env` na pasta do projeto com a sua chave do Gemini (dá pra pegar em https://aistudio.google.com/apikey):

```
GEMINI_API_KEY=cole_sua_chave_aqui
```

Roda o projeto:

```
python app.py
```

Depois é só abrir http://127.0.0.1:5000 no navegador.

## Aviso

Nunca suba o arquivo `.env` pro GitHub, ele tem a sua chave. O `.gitignore` do projeto já ignora ele.
