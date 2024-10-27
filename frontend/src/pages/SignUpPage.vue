<template>
  <div class="signup">
    <h2>Sign Up</h2>
    <form>
      <input type="text" placeholder="Username" />
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<style scoped>
.signup {
  background-color: #dc3545; /* Red */
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
  background-color: #c82333; /* Darker red */
  color: white;
  border: none;
  cursor: pointer;
}
</style>
