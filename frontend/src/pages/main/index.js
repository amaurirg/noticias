import React, { Component } from 'react';
import api from '../../services/api';
import './styles.css';

export default class Main extends Component {
    state = {
        dados_imprensa: {},
        dados_noticias: [],
    };

    componentDidMount() {
        this.loadRepos();
    }

    loadRepos = async () => {
        const url_params = "/uol"
        const response = await api.get(url_params);
        // console.log(response.data);
        const { imprensa, logo, atualizado_em, ...noticias } = response.data;
        this.setState({
            dados_imprensa: { imprensa, logo, atualizado_em },
            dados_noticias: noticias.noticias
        });
        // console.log(imprensa);
        // console.log(logo);
        // console.log(atualizado_em);
        // dados_noticias.noticias.map(noticia => (
        //     console.log(noticia.texto)
        // ));
        console.log(this.state.dados_noticias);
        // console.log(this.state.dados_noticias.noticias);
    }

    render() {
        const { dados_imprensa, dados_noticias } = this.state;
        return (
            <div className="container">
                <header>Notícias do Mundo</header>
                    <div className="imprensa-esquerda">
                        <img src={dados_imprensa.logo} alt="Logo" />
                        <p>Atualizado em {dados_imprensa.atualizado_em}hs</p>
                        <ul>
                            {dados_noticias.map((noticia, contador) => (
                                <div key={contador + 1} className="item">
                                    <img className="img-noticia" src={noticia.img} alt="Imagem da notícia" />
                                    <li><a href={noticia.link}>{noticia.texto}</a></li>
                                </div>
                            ))}
                        </ul>
                    </div>
                    <div className="imprensa-direita">
                        <img src={dados_imprensa.logo} alt="Logo" />
                        <p>Atualizado em {dados_imprensa.atualizado_em}hs</p>
                        <ul>
                            {dados_noticias.map((noticia, contador) => (
                                <div key={contador + 1} className="item">
                                    <img className="img-noticia" src={noticia.img} alt="Imagem da notícia" />
                                    <li><a href={noticia.link}>{noticia.texto}</a></li>
                                </div>
                            ))}
                        </ul>
                    </div>
                <footer></footer>
            </div>
        )
    }
}