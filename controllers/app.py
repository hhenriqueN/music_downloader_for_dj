from flask import Flask, render_template, request, url_for, redirect
from track_downloader import *
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.getcwd(), 'templates'),
    static_folder=os.path.join(os.getcwd(), 'static')  
)


@app.route('/')
def home():

    return render_template('index.html')

@app.route('/single')
def track_per_time():

    return render_template('single.html')

@app.route('/list')
def track_list():

    return render_template('list.html')

@app.route('/instalar_musica', methods=['POST'])
def instalar_musica():
    musica = request.form.get('musica')
    pasta_destino = 'downloads'
    
    # Variável de status para informar o frontend
    status_musica_instalada = "O Download de sua música foi completo!"

    # Inicia o processo de instalação
    buscar_e_baixar_musica(musica, pasta_destino)

    # Redireciona para a página de status de instalação (após a instalação)
    return render_template('download_musica_completo.html', status_musica_instalada=status_musica_instalada)

@app.route('/instalar_lista_musicas', methods=['POST'])
def instalar_lista_musicas():
    musicas = request.form.get('musicas')
    pasta_destino = 'downloads'

    # Variável de status para informar o frontend
    status_lista_instalada = "O Download de suas músicas foi completo!"

    # Inicia o processo de instalação
    lista_musicas = musicas.splitlines()
    for musica in lista_musicas:
        buscar_e_baixar_musica(musica, pasta_destino)

    # Redireciona para a página de status de instalação (após a instalação)
    return render_template('download_lista_completo.html', status_lista_instalada=status_lista_instalada)

    
    
    


if __name__ == '__main__':

    app.run(port=8000, debug=True)
