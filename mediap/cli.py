import json
from models import Track

comando = input("media> ")  # Exemplo de entrada: "library load musicas.json"[cite: 2]

if comando.startswith("library load "):
  # Extrai o caminho do arquivo (tudo o que vem depois de "library load ")[cite: 2]
    caminho_arquivo = comando.replace("library load ", "").strip()

    with open (caminho_arquivo, 'r',encoding='utf-8') as arq:
        dados=json.load(arq)

    tracks = [Track(**musica) for musica in dados["musicas"]]

    print(f"Sucesso: {len(tracks)} faixas carregadas!")

else:
    print(f"Erro, Digite um comando válido")
    #tem que fazer o loop