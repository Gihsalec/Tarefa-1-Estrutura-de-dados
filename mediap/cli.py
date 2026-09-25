import json
from models import Track

def carregar_biblioteca(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
        tracks_carregadas = [Track(**musica) for musica in dados["musicas"]]
        
        print(f"Sucesso: {len(tracks_carregadas)} faixas carregadas")
        return tracks_carregadas
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
    except Exception as erro:
            print(f"Erro: {erro}")

def listar_categoria (tipo, tracks):
    try:
        if tipo=="rating":
            ordem_rating=([],[],[],[],[])
            for ordem in tracks:
                if ordem.rating == 5:
                    ordem_rating[0].append(ordem)
                elif ordem.rating == 4:
                    ordem_rating[1].append(ordem)
                elif ordem.rating == 3:
                    ordem_rating[2].append(ordem)
                elif ordem.rating == 2:
                    ordem_rating[3].append(ordem)
                elif ordem.rating == 1:
                    ordem_rating[4].append(ordem)

            for lista_ordenada in ordem_rating:
                for cada_musica in lista_ordenada:
                    print(f"Título: {cada_musica.titulo} | Nota: {cada_musica.rating}")

        elif tipo == "titulo":
            ordem_titulo = tracks[:]
            
            n = len(ordem_titulo)
            for i in range(n-1):
                for j in range(n-1):
                    titulo_atual = ordem_titulo[j].titulo.lower()
                    titulo_proximo = ordem_titulo[j + 1].titulo.lower()
                    
                    if titulo_atual > titulo_proximo:
                        ordem_titulo[j], ordem_titulo[j + 1] = ordem_titulo[j + 1], ordem_titulo[j]

            for cada_musica in ordem_titulo:
                print(f"Título: {cada_musica.titulo} | Artista: {cada_musica.artista}")

        elif tipo == "artista":
            ordem_artista = tracks[:]
                    
            n = len(ordem_artista)
            for i in range(n-1):
                for j in range(n-1):
                    artista_atual = ordem_artista[j].artista.lower()
                    artista_proximo = ordem_artista[j + 1].artista.lower()
                            
                    if artista_atual > artista_proximo:
                        ordem_artista[j], ordem_artista[j + 1] = ordem_artista[j + 1], ordem_artista[j]
        
            for cada_musica in ordem_artista:
                print(f"Artista: {cada_musica.artista} | Título: {cada_musica.titulo}")

        elif tipo=="id":
            for cada_musica in tracks:
                print(f"Id: {cada_musica.id} | Título: {cada_musica.titulo}")


    except Exception as erro:
        print(f"Erro: {erro}")

tracks=[]
while True:
    comando = input("mediap> ").strip()

    if comando.startswith("library load "):
        caminho = comando.replace("library load ", "").strip()
        tracks = carregar_biblioteca(caminho)
    elif comando.startswith("library list"):
        if comando=="library list":
            categoria="id"
        else:
            categoria = comando.replace("library list by", "").strip()
        listar_categoria(categoria, tracks)
