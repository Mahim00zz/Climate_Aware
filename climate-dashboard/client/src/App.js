import React from 'react';
import ClimateInfo from './components/ClimateInfo';  // Import ClimateInfo component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Climate Awareness Dashboard</h1>
        <ClimateInfo />  {/* Render the climate data component */}
      </header>
    </div>
  );
}

export default App;
