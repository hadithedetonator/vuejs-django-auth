<template>
  <div class="login">
    <h2>Login</h2>
    <form>
      <input type="text" placeholder="Username" />
      <input type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<style scoped>
.login {
  background-color: #007bff; /* Blue */
  color: white;
  text-align: center;
  padding: 50px;
}

input {
  margin: 10px 0;
  padding: 10px;
  width: 200px;
}

button {
  padding: 10px 20px;
  background-color: #0056b3; /* Darker blue */
  color: white;
  border: none;
  cursor: pointer;
}
</style>
