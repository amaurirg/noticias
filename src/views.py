import requests
import bs4
import json
from datetime import datetime

class Fonte:
    def paginas_noticias(self, url):
        res = requests.get(url)
        res.raise_for_status()
        noticiario = bs4.BeautifulSoup(res.text, "html.parser")
        return noticiario

    def write_json(self, nome_arquivo, noticias):
        with open(nome_arquivo, "w") as f:
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))


class Band_News(Fonte):
    def __init__(self):
        self.nome = "Band News"
        self.url = "https://bandnewsfm.band.uol.com.br/noticias/"
        self.logo = "https://bandnewsfm.band.uol.com.br/wp-content/uploads/2020/05/logotipo-bandnewsfm_15anos.png"

    def principais_noticias(self):
        noticiario = self.paginas_noticias(self.url)
        div_main = noticiario.find_all("div", class_="td-module-thumb")
        data = []
        for item in div_main:
            img = item.find("img").get("src")
            texto = item.find("a").get("title").strip()
            link = item.find("a").get("href")
            data.append({"img": img, "texto": texto, "link": link})
        noticias = {'imprensa': self.nome, 'logo': self.logo,
                    "atualizado_em": datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'noticias': data}
        self.write_json("../data/band_news.json", noticias)


class Uol(Fonte):
    def __init__(self):
        self.nome = "Uol"
        self.url = "https://noticias.uol.com.br/"
        self.logo = "https://conteudo.imguol.com.br/c/home/layout/camaleao/web/logo.png"

    def principais_noticias(self):
        noticiario = self.paginas_noticias(self.url)
        div_main = noticiario.find_all("div", class_="thumbnails-wrapper")
        data = []
        for item in div_main:
            img = item.find("img")
            if not img:
                continue
            else:
                img = item.find("img").get("data-src")
            texto = item.getText().strip()
            link = item.find("a").get("href")
            data.append({"img": img, "texto": texto, "link": link})
        noticias = {'imprensa': self.nome, 'logo': self.logo,
                    "atualizado_em": datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'noticias': data}
        self.write_json("../data/uol.json", noticias)


Uol().principais_noticias()
Band_News().principais_noticias()
