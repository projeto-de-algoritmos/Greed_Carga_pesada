import Button from './components/Button';
import Input from './components/Input';
import List from './components/List';
import { useState} from 'react';
import { useForm } from "react-hook-form";
import './styles/global.css';

function App() {

  const [answers, setAnswers] = useState([]);
  const { register, handleSubmit, reset, formState:{errors} } = useForm();

  function onSubmit (data){
    setAnswers([...answers,data]);
    reset();
  }

  return (
    <>
      <div className="form">
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className="inputField">
            <Input 
              register={register("nome", {
                validate: value => !answers.some((item)=>item.nome===value) || 'Produto já existe!', 
                required: 'Campo obrigatório!'
              })} 
              inputPlaceholder = "Nome do produto" 
              inputTitle="Nome do produto"  
              type="text" 
              error={errors.nome}>
            </Input>
            <Input 
              register={register("peso", {
                validate: value => value > 0 || 'Peso inválido!', 
                required: 'Campo obrigatório!'
              })} 
              inputPlaceholder = "Peso do produto" 
              inputTitle="Peso do produto" 
              type="number"
              step="any"  
              error={errors.peso}>
            </Input>
            <Input 
              register={register("valor", {
                validate: value => value > 0 || 'Valor inválido!', 
                required: 'Campo obrigatório!'
              })} 
              inputPlaceholder = "Valor do produto" 
              inputTitle="Valor do produto" 
              type="number"
              step="any" 
              error={errors.valor}>
            </Input>
          </div>
          <Button title = 'Adicionar'/>
        </form>
      </div>
      <List answers={answers}/> 
    </>
  );
}

export default App;
