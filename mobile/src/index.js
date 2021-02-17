import React, { useState, useEffect } from 'react';
import api from './services/api';
import { View, Text, StyleSheet, FlatList, Image, StatusBar } from 'react-native';

export default function App() {
  const [uol, setUol] = useState({});
  // const [bandNews, setBandNews] = useState([]);
  // let lista = [];

  useEffect(() => {
    api.get('uol').then(response => {
      console.log(response.data.noticias)
      setUol(response.data.noticias);
      // uol.noticias.map(noticia =>
      //   console.log(noticia.id)
      // uol.noticias.map(noticia => lista.push(noticia.id));
      // )
    })
  }, []);

  // useEffect(() => {
  //   api.get('band_news').then(response => {
  //     // console.log(response.data);
  //     setBandNews(response.data);
  //   })
  // }, []);

  return (
    <>
      <StatusBar barStyle="light-content" backgroundColor="#7159c1" />
      <FlatList
        style={styles.container}
        data={uol}
        keyExtractor={project => project.id}
        renderItem={({ item: project }) => (
          <Text style={styles.project}>{project.texto}</Text>
        )}
      />
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginLeft: 10,
  },
  fontText: {
    color: '#FFF',
    fontSize: 20,
  },
  imgNoticia: {
    width: 100,
    height: 50,
    resizeMode: 'stretch'
  }
});