import logo from './hashedin-logo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="Ap-logo" alt="logo" />
        <h1>
	  Hashedin Universiy
        </h1>
          <h2>
HU Linker Deloitte Ritesh Zode
	 </h2>
        <a
          className="App-link"
          href="https://hashedin.com/"
          target="_blank"
          rel="noopener noreferrer"
        >
          About us
        </a>
      </header>
    </div>
  );
}

export default App;
