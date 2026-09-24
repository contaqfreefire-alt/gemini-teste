import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # <--- Nova biblioteca importada
from google import genai

app = FastAPI()

API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

# Mudamos a rota inicial para ler e exibir o nosso arquivo index.html
@app.get("/", response_class=HTMLResponse)
def raiz():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    return "<h1>Servidor online, mas arquivo index.html não foi encontrado.</h1>"

@app.get("/perguntar")
def perguntar_ia(mensagem: str):
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=mensagem,
        )
        return {"resposta": response.text}
    except Exception as e:
        return {"erro": str(e)}
