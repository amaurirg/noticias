import json

from flask import Flask, render_template, make_response

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    with open("../data/uol.json") as f:
        arquivo = json.load(f)
    return render_template(
        'index.html', logo=arquivo["logo"], data=arquivo["atualizado_em"],
        empresa=arquivo["imprensa"], noticias=arquivo['noticias'])


@app.route('/uol')
def uol():
    with open("../data/uol.json") as f:
        arquivo = json.load(f)
    r = make_response(arquivo)
    r.headers.add("Access-Control-Allow-Origin", "*")
#         response.header('X-Total-Count', count['count(*)']);

    return r


@app.route('/band_news')
def band_news():
    with open("../data/band_news.json") as f:
        arquivo = json.load(f)
    r = make_response(arquivo)
    r.headers.add("Access-Control-Allow-Origin", "*")
#         response.header('X-Total-Count', count['count(*)']);

    return r


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
