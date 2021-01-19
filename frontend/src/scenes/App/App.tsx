import React from 'react';
import logo from '../../assets/images/logo.svg';
import './App.css';
import { Provider } from 'react-redux';
import { store } from '../../store';

const App = () => (
  <Provider store={store}>
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>PuckwheatBarser</p>
      </header>
    </div>
  </Provider>
);

export default App;
