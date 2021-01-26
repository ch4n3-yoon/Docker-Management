import logo from './logo.svg';
import './App.css';
import React from 'react';
import DockerCompose from './pages/docker-compose';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Login from './pages/Login';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Login}/>
        {/*<Route path="/project" component={P}/>*/}
      </Switch>
    </BrowserRouter>
  );
}

export default App;
