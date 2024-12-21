import React from 'react';
import ConfigDisplay from './components/ConfigDisplay';  // Import the ConfigDisplay component
import './App.css';  // Keep the CSS for styling

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Climate Awareness Dashboard</h1>
        <p>Welcome to the Climate Awareness Dashboard. Here you'll get real-time data and actionable insights to reduce your carbon footprint.</p>
        {/* Insert the ConfigDisplay component to show your configuration */}
        <ConfigDisplay />
        
        {/* You can also add more components for climate data or resources */}
      </header>
    </div>
  );
}

export default App;
