from flask import Flask, render_template
from controllers import routes
import requests

app = Flask(__name__, template_folder='views')

routes.init_app(app)

@app.route("/apifilmes")
@app.route("/apifilmes/<film_id>")
def apifilmes(film_id=None):
    if film_id:
        resp = requests.get(f"api/films/{film_id}", timeout=10)
        if resp.ok:
            filmInfo = resp.json()
            return render_template("filmesinfo.html", filmInfo=filmInfo)
        else:
            return f"Filme com ID {film_id} não encontrado.", resp.status_code
    else:
        resp = requests.get(f"api/films", timeout=10)
        if resp.ok:
            filmList = resp.json()
            return render_template("apifilmes.html", filmList=filmList)
        else:
            return f"Erro: {resp.status_code}", resp.status_code

if __name__ == "__main__":
    app.run(debug=True)