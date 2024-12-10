import os
import pandas as pd
from youtubesearchpython import VideosSearch
import yt_dlp

# Função para carregar músicas de um arquivo de texto
def carregar_musicas_do_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        musicas = f.read().splitlines()
    return musicas

# Função para carregar músicas de um arquivo CSV
def carregar_musicas_de_csv(arquivo):
    df = pd.read_csv(arquivo)
    return df['musica'].tolist()

# Função para baixar o áudio em MP3
def baixar_audio(url, nome_arquivo, pasta_destino):
    caminho_completo = os.path.join(pasta_destino, f'{nome_arquivo}')
    
    if not os.path.exists(caminho_completo):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': caminho_completo,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    else:
        print(f"'{caminho_completo}' já existe. Pulando download.")


# Função para buscar e baixar uma única música por vez
def buscar_e_baixar_musica(musica, pasta_destino):
    try:
        search = VideosSearch(musica, limit=1)
        resultado = search.result()

        if resultado and len(resultado['result']) > 0:
            video_info = resultado['result'][0]
            titulo = video_info['title']
            url = video_info['link']

            nome_arquivo = f"{titulo}"
            print(f"Baixando: {titulo} ({url})")

            baixar_audio(url, nome_arquivo, pasta_destino)
        else:
            print(f"Música '{musica}' não encontrada.")
    except Exception as e:
        print(f"Erro ao processar '{musica}': {e}")


# Função para buscar e baixar uma lista de musicas
def buscar_e_baixar_musicas(musica, indice, pasta_destino):
    try:
        search = VideosSearch(musica, limit=1)
        resultado = search.result()

        if resultado and len(resultado['result']) > 0:
            video_info = resultado['result'][0]
            titulo = video_info['title']
            url = video_info['link']

            nome_arquivo = f"{indice + 1:02d} - {titulo}"
            print(f"Baixando: {titulo} ({url})")

            baixar_audio(url, nome_arquivo, pasta_destino)
        else:
            print(f"Música '{musica}' não encontrada.")
    except Exception as e:
        print(f"Erro ao processar '{musica}': {e}")

# # Definir pasta de destino
# pasta_destino = 'downloads'

# # Garantir que a pasta de destino existe
# os.makedirs(pasta_destino, exist_ok=True)

# # Exemplo de uso: Carregar músicas de um arquivo de texto ou CSV

# # Para carregar de um arquivo de texto:
# musicas = carregar_musicas_do_arquivo('musicas.txt')

# # OU para carregar de um arquivo CSV, descomente a linha abaixo e comente a linha anterior:
# # musicas = carregar_musicas_de_csv('musicas.csv')

# # Loop para buscar e baixar cada música da lista
# for indice, musica in enumerate(musicas):
#     buscar_e_baixar_musicas(musica, indice, pasta_destino)

# print("Download concluído!")
