
import './App.css';
import axios from 'axios';
import React from 'react';

function App() {
  
  const  [users, setUsers] = React.useState([])
  function getUsers(){
    axios.get('http://localhost:8001/api/v1/users')
  .then(function (response) {
      setUsers(response.data)
    console.log(response);
  })
  .catch(function (error) {
    
    console.log(error);
  })
  }
  function deleteUser(id){
    axios.delete('http://localhost:8001/api/v1/users/' + id)
  .then(function (response) {
    getUsers();
  console.log(response);
  })
  .catch(function (error) {
  
  console.log(error);
  })
}
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Viktor is Awsome
        </p>
        <button
        onClick={()=> getUsers()
        }
        >Click me</button>
        <div>{users.map(user => {
          return <div key={user.id} >
            <p className='userId'>ID : {user.id} </p>
            <p>First Name : {user.first_name}</p>
            <button
            onClick={()=> deleteUser(user.id)
            }
            >delete</button>
            
          </div>
          
        })}
        </div>
      </header>
    </div>
  );
}

export default App;

