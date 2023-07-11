import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Signup() {
  const [username, setUsername] = useState('');
  const [name, setName] = useState('');
  const [role, setRole] = useState('New Collector');
  const [signedUp, setSignedUp] = useState(false);

  const handleSignup = (e) => {
    e.preventDefault();

    setSignedUp(true);
  };

  if (signedUp) {
    return <Link to="/collections/:id">Go to Collections</Link>;
  }

  return (
    <form className="pure-form pure-form-stacked" onSubmit={handleSignup}>
      <fieldset>
        <legend>Log In</legend>
        <label htmlFor="stacked-email">Username</label>
        <input
          type="email"
          id="stacked-email"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <span className="pure-form-message"></span>
        <label htmlFor="stacked-password">Name</label>
        <input
          type="password"
          id="stacked-password"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <label htmlFor="stacked-state">Role</label>
        <select
          id="stacked-state"
          value={role}
          onChange={(e) => setRole(e.target.value)}
        >
          <option>New Collector</option>
          <option>Art Lover</option>
          <option>Not Sure</option>
        </select>
        <label htmlFor="stacked-remember" className="pure-checkbox">
          <input type="checkbox" id="stacked-remember" /> Remember me
        </label>
        <button type="submit" className="pure-button pure-button-primary">
          Sign in
        </button>
      </fieldset>
    </form>
  );
}

export default Signup;




// function Signup(){

//     return(
//         <form class="pure-form pure-form-stacked">
//     <fieldset>
//         <legend>Log In</legend>
//         <label for="stacked-email">Username</label>
//         <input type="email" id="stacked-email" placeholder="Username" />
//         <span class="pure-form-message"></span>
//         <label for="stacked-password">Name</label>
//         <input type="password" id="stacked-password" placeholder="Name" />
//         <label for="stacked-state">Role</label>
//         <select id="stacked-state">
//             <option>New Collector</option>
//             <option>Art Lover</option>
//             <option>Not Sure</option>
//         </select>
//         <label for="stacked-remember" class="pure-checkbox">
//             <input type="checkbox" id="stacked-remember" /> Remember me
//         </label>
//         <button type="submit" class="pure-button pure-button-primary">Sign in</button>
//     </fieldset>
// </form>
//     );
//   }

// export default Signup