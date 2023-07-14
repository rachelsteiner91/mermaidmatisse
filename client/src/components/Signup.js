import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Signup() {
  const [username, setUsername] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState(''); // Add password state
  const [role, setRole] = useState('New Collector');
  const [signedUp, setSignedUp] = useState(false);

  const handleSignup = async (e) => {
    e.preventDefault();

    // Validate password
    if (password === '') {
      console.log('Password cannot be empty');
      return;
    }

    // Create the user object
    const user = {
      username,
      name,
      role,
      password,
    };

    try {
      // Send a POST request to your backend signup endpoint
      const response = await fetch('http://localhost:5555/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
      });

      if (response.ok) {
        // Signup successful, perform the login process
        // You may need to adjust the login endpoint and payload according to your backend implementation
        const loginResponse = await fetch('http://localhost:5555/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: user.username,
            password: user.password,
          }),
        });

        if (loginResponse.ok) {
          // Login successful, update the signedUp state
          setSignedUp(true);
        } else {
          // Handle login error
          console.log('Login failed');
        }
      } else {
        // Handle signup error
        console.log('Signup failed');
      }
    } catch (error) {
      // Handle any network or server errors
      console.log('Error:', error.message);
    }
  };

  if (signedUp) {
    return <Link to="/collections">Go to Collections</Link>;
  }
  return (
    <form className="pure-form pure-form-stacked" onSubmit={handleSignup}>
      <fieldset>
        <legend>Sign Up</legend>
        <label htmlFor="stacked-email">Username</label>
        <input
          type="username"
          id="stacked-username"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <span className="pure-form-message"></span>
        <label htmlFor="stacked-password">Name</label>
        <input
          type="name"
          id="stacked-name"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <label htmlFor="stacked-password">Password</label>
        <input
          type="password"
          id="stacked-password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
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
 