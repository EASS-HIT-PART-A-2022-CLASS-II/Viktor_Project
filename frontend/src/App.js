
import './App.css';
import axios from 'axios';
import React from 'react';

function App() {
  
  const  [users, setUsers] = React.useState([])
  const [name, setName] = React.useState('');
  const [lastName, setLastName] = React.useState('');
  const [user, setUser] = React.useState(false);
  const [admin , setAdmin] = React.useState(false);
  const [gender , setGender] = React.useState();
  const [count, setCount] =React.useState();


  


  function getUsers(){
    axios.get('http://localhost:80/api/v1/users')
  .then(function (response) {
      setUsers(response.data);
      showNumer();
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
    axios.post('http://localhost:80/api/v1/users/random?num=1')
  .then(function (response) {
    getUsers();
  console.log(response);
  })
  .catch(function (error) {
  
  console.log(error);
  })

  }
  function createNewUser(){
    console.log("User is Created")
    let roles = [];
    if(admin) roles.push('admin')
    if(user) roles.push('user')
    console.log(roles)
  

    const userData = {
      "first_name": name,
      "last_name": lastName,
      "gender": gender,
    };
    if(roles !== []){userData.roles = roles}

    
    console.log(userData.first_name);
    axios.post('http://localhost:80/api/v1/users',userData)
    .then(function (response) {
      getUsers();
    console.log(response);
    })
    .catch(function (error) {
    
    console.log(error);
    })
  }
  function showNumer(){
    axios.get('http://localhost:80/api/v1/users/number')
    .then(function (response) 
    {console.log(response);
      setCount(response.data);
  })

  }


  return (
    <div className="App">
      <header className="App-header">
        <p>
          Viktor Project
        </p>
        
        <div className='userCounter'type="text" > Users in DB: {count} <p></p></div>
        <button
        onClick={()=> getUsers()
        }
        >Display</button><br></br>
        <button
        onClick={()=> createRandomUser()
        }
        >Random</button>
        <form  className='userForm' id="user-form" onSubmit={(e) => {e.preventDefault(); createNewUser(); setAdmin(false); setLastName(""); setName("")}}>
          <label for="first-name">First Name: </label>
          <input onChange = {(e) => {setName(e.target.value)}} value = {name} type="text" /><br/>
          <label for="last-name">Last Name: </label>
          <input onChange = {(e) => {setLastName(e.target.value)}} value = {lastName} type="text" /><br/>
          <label for="gender">Gender:</label><br/>
          <input type="radio" onChange ={e => {setGender('male'); }} checked={gender === 'male'}/> Male<br/>
          <input type="radio"onChange={e => setGender('female')} checked={gender === 'female'}/> Female<br/>
          <label for="roles">Roles:</label><br/>
          <input type="checkbox" defaultChecked={user} onChange={e => {setUser(e.target.value);}} checked={user}  /> User<br/>
          <input type="checkbox" onChange={e => {setAdmin(e.target.value);}} checked={admin}/> Admin<br/>
          <button type="submit">Submit</button>
        </form> 
        <div className='displayUsers'>{users.map(user => {
          return <div key={user.id} >
            <p className='userId'>ID : {user.id} </p>
            <p className='userName'>Name : {user.first_name}  {user.last_name}</p>
            <p className='userName'>Role : {user.roles[0]} {user.roles[1]}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Gender: {user.gender} </p>
            <button
            onClick={(e)=> { 
              deleteUser(user.id);
              }
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

