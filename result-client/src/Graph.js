import React from 'react';
import {scaleLinear, scaleOrdinal} from 'd3-scale';
import {schemeCategory10} from 'd3-scale-chromatic';

const Graph = ({size, data, qIndex}) => {
  const padding = size/10;
  const innerDim = {width: size - padding*2, height: size - padding*2}

  const xScale = scaleLinear()
    .domain([0, data.length])
    .range([0, innerDim.width]);
 
  const yScale = scaleLinear()
    .domain([0, 10])
    .range([0, innerDim.height]);
  
  const colorScale = scaleOrdinal(schemeCategory10);

  return <svg width={size} height={size}>
    <g transform={`translate(${padding},${padding})`}>
      <g>
        <text fontWeight="bold" y={-20}>Resultat fråga {qIndex + 1}</text>
        <line
          x1={0}
          x2={0}
          y1={0}
          y2={innerDim.height}
          stroke="black"
        />
        {yScale.ticks(5).map((c, i) => {
          return <g key={i} transform={`translate(0, ${yScale(10) - yScale(c)})`}>
            <text x={-5} y={5} textAnchor="end">{c}</text>
            <line
              x1={-3}
              x2={3}
              y1={0}
              y2={0}
              stroke="black"
            />
          </g>
        })}
      </g>
      <g transform={`translate(${0},${innerDim.height})`}>
        <text fontWeight="bold" x={innerDim.width} y={16}>Bord</text>
        <line
          x1={0}
          x2={innerDim.width}
          y1={0}
          y2={0}
          stroke="black"
        />
      </g>
      <g>
        {data.map((res, i) => {
          return <g
            key={i}

          >
          </g>
        })}
      </g>
      {data.map((p, i) => {
        return <g key={i} transform={`translate(${xScale(i) + padding/3},${yScale(p)})`}>
          <rect
            width={20}
            height={yScale(10) - yScale(p)}
            fill={colorScale(i)}
          />
          <text
            textAnchor="middle"
            x={10}
            y={yScale(10) - yScale(p) + 16}
          >
            {i+1}
          </text>
        </g>
      })}
    </g>
  </svg>
}

export default Graph;