import React from 'react';
import './styles.css'

function Card({nome, peso, valor, deleteCard}){

  return(
    <div className="card" > 
    {/* {`${nome} ${peso} ${valor}`} */}
    <span>Nome: {nome}</span>
    <span>Peso: {peso}</span>
    <span>Valor: {valor}</span>
    <div className="deleteBtnContainer">
      <button className="deleteBtn" onClick={deleteCard}>x</button>
    </div>
    </div>
  );
}

export default Card;