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

    buscar_e_baixar_musica(musica, pasta_destino)

    return '', 200

@app.route('/instalar_lista_musicas', methods=['POST'])
def instalar_lista_musicas():

    musicas = request.form.get('musicas')

    pasta_destino = 'downloads'

    lista_musicas = musicas.splitlines()

    # Imprime a lista de músicas
    print("Músicas recebidas:")
    for musica in lista_musicas:
        print(musica)


    for indice, musica in enumerate(lista_musicas):
        buscar_e_baixar_musicas(musica, indice, pasta_destino)

    return '', 200

    
    
    


if __name__ == '__main__':

    app.run(port=8000, debug=True)