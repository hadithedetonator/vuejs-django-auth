<template>
  <LayoutDefault>
    <div v-if="isAuthenticated">
      <TemplatePokemonList />
    </div>
    <div v-else>
      <p>You need to log in to view Pokémon.</p>
      <button @click="redirectToLogin">Login</button>
    </div>
  </LayoutDefault>
</template>

<script>
import { computed } from "vue"; // Import computed
import LayoutDefault from "../layout/LayoutDefault.vue";
import TemplatePokemonList from "../components/templates/TemplatePokemonList.vue";
import { useAuthStore } from "../store/authStore";
import { useRouter } from "vue-router";

export default {
  name: "PageHome",
  components: {
    LayoutDefault,
    TemplatePokemonList,
  },
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();

    // Check if the user is authenticated
    const isAuthenticated = computed(() => authStore.accessToken !== null);

    // Redirect to login if the user is not authenticated
    const redirectToLogin = () => {
      router.push("/login");
    };

    return {
      isAuthenticated,
      redirectToLogin,
    };
  },
};
</script>
