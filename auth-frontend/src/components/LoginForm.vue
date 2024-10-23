<template>
  <div class="login-form">
    <img alt="Login icon" src="/login.png">
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Log In</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
    <div class="form-footer">
      <a href="#">Forgot Password?</a>
      <span> | </span>
      <a href="#">Create an Account</a>
    </div>
  </div>
</template>

<script>
import axios from '../axios'; // Import your Axios instance

export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('login/', {
          username: this.username,
          password: this.password
        });
        alert(response.data.message); // Show success message
        // Optionally store token or redirect
      } catch (err) {
        this.error = err.response.data.error || 'Login failed';
      }
    }
  }
}
</script>

<style scoped>
/* Your existing styles */
</style>
