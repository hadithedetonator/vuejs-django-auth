<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Username" />
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { useAuthStore } from "../store/authStore";

export default {
  setup() {
    const authStore = useAuthStore();
    const username = ref("");
    const email = ref("");
    const password = ref("");

    const register = () => {
      authStore.register({
        username: username.value,
        email: email.value,
        password: password.value,
      });
    };

    return { username, email, password, register };
  },
};
</script>
