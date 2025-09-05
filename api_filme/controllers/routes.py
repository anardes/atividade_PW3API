from flask import render_template
import urllib.request
import json
import requests

def init_app(app):
    @app.route('/')
    def home():
        return render_template('base.html')
    
    @app.route('/apifilmes')
    @app.route('/apifilmes/<film_id>')
    def apifilmes(film_id=None):
        base_url = "https://ghibliapi.vercel.app/films"

        if film_id:
            # Busca detalhes de um filme específico
            resp = requests.get(f"{base_url}/{film_id}", timeout=10)
            if resp.ok:
                filmInfo = resp.json()
                return render_template('filmesinfo.html', filmInfo=filmInfo)
            else:
                return f"Filme com ID {film_id} não encontrado.", resp.status_code
        else:
            # Busca lista de todos os filmes
            resp = requests.get(base_url, timeout=10)
            if resp.ok:
                filmList = resp.json()
                return render_template('apifilmes.html', filmList=filmList)
            else:
                return f"Erro: {resp.status_code}", resp.status_code