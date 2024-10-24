<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
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
    const password = ref("");

    const login = () => {
      authStore.login({ username: username.value, password: password.value });
    };

    return { username, password, login };
  },
};
</script>
