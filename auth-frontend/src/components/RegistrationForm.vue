<template>
    <div class="registration-form">
      <img alt="Registration icon" src="/login.png">
      <form @submit.prevent="handleRegistration">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div class="form-group">
          <label for="confirmPassword">Confirm Password</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required>
        </div>
        <button type="submit">Register</button>
      </form>
      <div class="form-footer">
        <span>Already have an account? </span>
        <a href="#">Log In</a>
      </div>
    </div>
  </template>
  

  <script>
  import axios from '../axios'; // Import your Axios instance
  
  export default {
    name: 'RegistrationForm',
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        error: ''
      };
    },
    methods: {
      async handleRegistration() {
  if (this.password !== this.confirmPassword) {
    this.error = 'Passwords do not match!';
    return;
  }

  try {
    const response = await axios.post('register/', {
      username: this.username,
      email: this.email,
      password: this.password
    });
    
    alert('Registration successful!');
    // Reset the form fields
    this.username = '';
    this.email = '';
    this.password = '';
    this.confirmPassword = '';
  } catch (err) {
    if (err.response) {
      this.error = err.response.data.error || 'Registration failed';
    } else if (err.request) {
      this.error = 'No response from server. Please check your connection.';
    } else {
      this.error = 'An unexpected error occurred: ' + err.message;
    }
  }
}
    },
    watch: {
    username(newValue) {
      console.log('Username:', newValue);
    },
    password(newValue) {
      console.log('Password:', newValue);
    }
    
    }
  }
  </script>
  
  <style scoped>
  .registration-form {
    max-width: 400px;
    margin: 100px auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    color: #555;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: 6px;
    border: 1px solid #ddd;
    border-radius: 5px;
    transition: border-color 0.3s;
  }
  
  input[type="text"]:focus,
  input[type="email"]:focus,
  input[type="password"]:focus {
    border-color: #007bff;
    outline: none;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #112235;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  .form-footer {
    text-align: center;
    margin-top: 10px;
  }
  
  img {
    height: 250px;
    width: 250px;
    margin-bottom: 5px;
  }
  </style>
  