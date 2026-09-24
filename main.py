import os
from fastapi import FastAPI
from google import genai

app = FastAPI()

# O Render vai ler a chave configurada no painel de controle deles de forma segura
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

@app.get("/")
def raiz():
    return {"status": "Servidor da IA online no Render!"}

@app.get("/perguntar")
def perguntar_ia(mensagem: str):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=mensagem,
        )
        return {"resposta": response.text}
    except Exception as e:
        return {"erro": str(e)}
