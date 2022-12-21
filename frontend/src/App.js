
import './App.css';
import axios from 'axios';
import React from 'react';

function App() {
  
  const  [users, setUsers] = React.useState([])
  function getUsers(){
    axios.get('http://localhost:80/api/v1/users')
  .then(function (response) {
      setUsers(response.data)
    console.log(response);
  })
  .catch(function (error) {
    
    console.log(error);
  })
  }
  function deleteUser(id){
    axios.delete('http://localhost:80/api/v1/users/' + id)
  .then(function (response) {
    getUsers();
  console.log(response);
  })
  .catch(function (error) {
  
  console.log(error);
  })
  }
  function createRandomUser(){
    axios.post('http://localhost:80/api/v1/users/random' + '?num=1')
  .then(function (response) {
    getUsers();
  console.log(response);
  })
  .catch(function (error) {
  
  console.log(error);
  })
  }
  function createNewUser(){
    function handleFormSubmit(event) {
      // Prevent the form from reloading the page
      event.preventDefault();
    
      // Get the form data
      const firstName = document.getElementById('first-name').value;
      const lastName = document.getElementById('last-name').value;
      const gender = document.querySelector('input[name="gender"]:checked').value;
      const roles = [];
      const roleElements = document.querySelectorAll('input[name="roles"]:checked');
      for (let i = 0; i < roleElements.length; i++) {
        roles.push(roleElements[i].value);
      }

      // Create a JSON object with the form data
      const userData = {
        "first_name": firstName,
        "last_name": lastName,
        "gender": gender,
        "roles": roles
      };
    
      // Add the data to the JSON file
      // TODO: Add code here to write the userData object to a JSON file
    
      // Clear the form
      event.target.reset();
    }
    

  }


  return (
    <div className="App">
      <header className="App-header">
        <p>
          Viktor Project
        </p>
        <button
        onClick={()=> getUsers()
        }
        >Display</button>
        <button
        onClick={()=> createRandomUser()
        }
        >Random</button>
        <form id="user-form">
          <label for="first-name">First Name:</label><br/>
          <input type="text" id="first-name" name="first-name"/><br/>
          <label for="last-name">Last Name:</label><br/>
          <input type="text" id="last-name" name="last-name"/><br/>
          <label for="gender">Gender:</label><br/>
          <input type="radio" id="male" name="gender" value="male"/> Male<br/>
          <input type="radio" id="female" name="gender" value="female"/> Female<br/>
          <label for="roles">Roles:</label><br/>
          <input type="checkbox" id="user" name="roles" value="user"/> User<br/>
          <input type="checkbox" id="admin" name="roles" value="admin"/> Admin<br/>
          <input type="submit" value="Submit"/>
        </form> 
        <div className='displayUsers'>{users.map(user => {
          return <div key={user.id} >
            <p className='userId'>ID : {user.id} </p>
            <p className='userName'>Name : {user.first_name}  {user.last_name}</p>
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

