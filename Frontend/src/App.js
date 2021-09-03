import Button from './components/Button';
import Input from './components/Input';
import List from './components/List';
import axios from 'axios';
import { useState} from 'react';
import { useForm } from "react-hook-form";
import './styles/global.css';

function App() {

    const [answers, setAnswers] = useState([]);
    const { register, handleSubmit, reset, formState:{errors} } = useForm();
    const {
        register: register1,
        formState: { errors: errors1 },
        handleSubmit: handleSubmit1,
    } = useForm();

    function onSubmit (data){
        setAnswers([...answers,data]);
        reset();
    }
    function sendButton(pesoMax){
        const reqBody = {
            pesoMax,
            data:answers
        }
        console.log(reqBody);
        const headers = {'content-type': 'application/json'}     
        axios.post('http://127.0.0.1:5000/charge/', reqBody, headers)     
            .then(function (response) {       
                console.log(response);     })
            .catch(error => {       
                console.log(error)   })
    }

    return (
        <>
        <div className="form">
            <form key={0} onSubmit={handleSubmit(onSubmit)}>
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
      <List answers={answers} deleteCard={setAnswers}/>
      <form className="sendForm" onSubmit={handleSubmit1(sendButton)}>
          <div className="sendFormContainer">
              <Input 
              register={register1("pesoMax", {
              validate: value => value > 0 || 'Valor inválido!'
              })} 
              inputPlaceholder = "Peso max" 
              inputTitle="Peso máximo suportado" 
              type="number"
              step="any" 
              error={errors1.pesoMax}>
          </Input>
      </div>

      <Button title = 'Calcular'/> 

  </form>
    </>
    );
}

export default App;
