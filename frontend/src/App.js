import logo from './logo.svg';
import './App.css';
import React from 'react';
import DockerCompose from './pages/docker-compose';
import { BrowserRouter, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Route exact path="/" component={DockerCompose}/>
    </BrowserRouter>
  );
}

export default App;
