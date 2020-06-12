import json

from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    # uol = Uol("Uol", "https://noticias.uol.com.br/")
    # noticias = uol.principais_noticias()
    with open("../data/uol.json") as f:
        noticias = json.load(f)
    return render_template('index.html', logo=noticias["Uol"], empresa="Uol", noticias=noticias["noticias"])


@app.route('/api')
def api():
    # uol = Uol("Uol", "https://noticias.uol.com.br/")
    # noticias = uol.principais_noticias()
    with open("../data/uol.json") as f:
        return json.load(f)
    return json.dump(noticias, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
