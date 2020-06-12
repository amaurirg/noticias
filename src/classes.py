import requests
import bs4
import json


class Fonte:
    def __init__(self, nome, url):
        self.nome = nome
        self.url = url

    def paginas_noticias(self):
        res = requests.get(self.url)
        res.raise_for_status()
        noticiario = bs4.BeautifulSoup(res.text, "html.parser")
        return noticiario

    def write_json(self, nome_arquivo, noticias):
        with open(nome_arquivo, "w") as f:
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))


class Band_News(Fonte):
    def __init__(self, nome, url):
        super().__init__(nome, url)

    def principais_noticias(self):
        noticiario = self.paginas_noticias()
        items = noticiario.select(".item-details h3 a")
        noticias = {self.nome: [{"texto": item.getText().strip(), "link": item.get("href")} for item in items]}
        self.write_json("../data/band_news.json", noticias)
        # return json.dump(noticias, indent=4, ensure_ascii=False)


class Uol(Fonte):
    def __init__(self, nome, url):
        super().__init__(nome, url)
        self.logo = "https://conteudo.imguol.com.br/c/home/layout/camaleao/web/logo.png"

    def principais_noticias(self):
        noticiario = self.paginas_noticias()
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
        noticias = {self.nome: self.logo, 'noticias': data}
        self.write_json("../data/uol.json", noticias)


# Uol
uol = Uol("Uol", "https://noticias.uol.com.br/")
uol.principais_noticias()

# bandnews = Band_News("Band News", "https://bandnewsfm.band.uol.com.br/noticias/")
# bandnews.principais_noticias()
