import React from 'react';
import './styles.css'
import Card  from '../Card'

function List({answers}){

  return(
    <div>
      {answers.map((item)=><Card key={item.nome} {...item}></Card>)}
    </div>
  );
}

export default List