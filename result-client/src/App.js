import React, { Component, useState, useEffect } from 'react';
import Graphs from './Graphs';
import './App.css';


const App = props => {
  const [data, setData] = useState([]);
  const fetchData = async () => {
    fetch('/api/results')
      .then(response => response.json())
      .then(data => {
        const questionIndices = Object.keys(data[0].responses[0]);
        const newData = questionIndices.map(qIndex => {
          return data.map(table => {
            return table.responses.reduce((total, current, _, src) => {
              return total + (parseInt(current[qIndex]) / src.length)
            }, 0)
          })
        });
        setData(newData);
      })
  };
  
  useEffect(() => {
    fetchData()
  }, []);

  return (
    <div className="App">
      <Graphs data={data} />
    </div>
  );
}

export default App;
