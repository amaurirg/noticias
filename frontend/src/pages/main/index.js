import React, { Component } from 'react';
import api from '../../services/api';


export default class Main extends Component {
    state = {
        dados_imprensa: {},
        dados_noticias: [],
    };

    componentDidMount() {
        this.loadRepos();
    }

    loadRepos = async () => {
        const url_params = "/api"
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
            <div className="dados_imprensa">
                <h1>{dados_imprensa.imprensa}</h1>
                <img src={dados_imprensa.logo} alt="Logo" />
                <p>Atualizado em {dados_imprensa.atualizado_em}hs</p>
                <ul>
                    {dados_noticias.map((noticia, contador) => (
                        <li key={contador+1}>{noticia.texto}</li>
                    ))}
                </ul>
            </div>
        )
    }
}