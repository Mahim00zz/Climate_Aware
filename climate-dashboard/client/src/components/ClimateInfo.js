import React, { useState, useEffect } from 'react';
import axios from 'axios';  

const ClimateInfo = () => {
  
  const [climateData, setClimateData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    
    const fetchClimateData = async () => {
      try {
        const response = await axios.get('/api/climate-data', {
          params: {
            lat: "40.7128",  // For example, New York's latitude
            lon: "-74.0060"  // For example, New York's longitude
          },
        });
        setClimateData(response.data);
      } catch (error) {
        setError("Failed to fetch climate data.");
      } finally {
        setLoading(false);
      }
    };

    fetchClimateData();  // Call function to fetch data on component mount
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (!climateData) {
    return <div>No climate data available.</div>;
  }

  // Example of displaying some of the fetched data
  return (
    <div>
      <h2>Climate Data</h2>
      <p>Location: {climateData.name}</p>
      <p>Temperature: {climateData.main.temp}°C</p>
      <p>Humidity: {climateData.main.humidity}%</p>
      <p>Weather: {climateData.weather[0].description}</p>
    </div>
  );
};

export default ClimateInfo;
