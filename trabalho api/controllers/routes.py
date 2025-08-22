from flask import render_template, request, url_for, redirect
import urllib
import json

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/apifilmes', methods=['GET', 'POST'])
    @app.route('/apifilmes/<int:id>', methods=['GET', 'POST'])
    def api_filmes(id=None):
        url = 'https://ghibliapi.vercel.app/films'
        response = urllib.request.urlopen(url)
        apiData = response.read()
        filmesList = json.loads(apiData)
        # Se id existir (ou seja, foi informado parâmetro)
        if id:
            filmesInfo = []
            for filmes in filmesList:
                if filmes ['id'] == id:
                    filmesInfo = filmes
                    break
            if filmesInfo:
                return render_template('filmesinfo.html', filmesInfo=filmesInfo)
            else:
                return f'Filme com a ID {id} não foi encontrado.'
        else:
            return render_template('apifilmes.html', filmesList=filmesList)