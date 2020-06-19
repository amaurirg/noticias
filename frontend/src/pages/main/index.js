import React, { Component } from 'react';
import api from '../../services/api';

export default class Main extends Component {
    state = {
        noticias: []
    };

    componentDidMount() {
        this.loadRepos();
    }

    loadRepos = async () => {
        const url_params = "/api"
        const response = await api.get(url_params);
        console.log(response.data);
        this.setState({noticias: response.data});
    }

    render() {
        const {noticias} = this.state;
        return (
            <div>
                <img src={noticias.logo} alt=""/>
                <ul>
                {noticias.map(noticia => (
                    console.log(noticia)
                ))}
                </ul>
            </div>
        )
    }
}