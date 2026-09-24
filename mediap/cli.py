import json
from models import Track

def carregar_biblioteca(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
        tracks = [Track(**musica) for musica in dados["musicas"]]
        
        print(f"Sucesso: {len(tracks)} faixas carregadas")
        return tracks
    except FileNotFoundError:
        print(f"Erro: O arquivo {"caminho_arquivo"} não foi encontrado.")

while True:
    comando = input("mediap> ").strip()

    if comando.startswith("library load "):
        caminho = comando.replace("library load ", "").strip()
        biblioteca = carregar_biblioteca(caminho)
