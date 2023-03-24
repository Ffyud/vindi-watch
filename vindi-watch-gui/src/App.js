import './App.css';

let results = require("./results/result.json")
function App() {

  return (
    <div className="App">
      <h1>Vindi-watch monitort nieuws over Vindicat</h1>
      <div className="categories">
        <span className="category mishandeling">2x mishandeling</span>
        <span className="category asociaal">5x asociaal gedrag</span>
        <span className="category grensoverschrijdend">5x grensoverschrijdend gedrag</span>
        <span className="category dierenmishandeling">1x dierenmishandeling</span>
        <span className="category financieel">3x financieel</span>
        <span className="category overig">3x financieel</span>
      </div>
      <h2>Laatste nieuws:</h2>
      <ul>
        {results.map((element, key) => {
          return <li key={key}>{element.title}</li>
        })}
      </ul>
    </div>
  );
}

export default App;
