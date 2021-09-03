import React from 'react';
import './styles.css'

function Card({nome, peso, valor}){

  return(
    <div>
      <p>{`${nome} ${peso} ${valor}`}</p>
    </div>
  );
}

export default Card;