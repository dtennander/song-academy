import React from 'react';
import Graph from './Graph';

const Graphs = props => {
  return <div className="graphs">
    {props.data.map((results, i) => {
      return <Graph key={i} size={600} data={results} qIndex={i}/>
    })}
  </div>
};

export default Graphs;