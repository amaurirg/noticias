import requests
import bs4
import json



def paginas_noticias(nome, url):
    res = requests.get(url)
    res.raise_for_status()
    noticiario = bs4.BeautifulSoup(res.text, "html.parser")
    return noticiario


def write_json(noticias):
    with open("noticias.txt", "w") as f:
        f.write(json.dumps(noticias, indent=4, ensure_ascii=False))


def band_news():
    bandnews = {"nome": "Band News", "url": "https://bandnewsfm.band.uol.com.br/noticias/"}
    noticiario = paginas_noticias(bandnews["nome"], bandnews["url"])
    items = noticiario.select(".item-details h3 a")
    noticias = {bandnews["nome"]: [{"texto": item.getText(), "link": item.get("href")} for item in items]}
