import { createRouter, createWebHistory } from "vue-router";
import PageHome from "../pages/PageHome.vue";
import PageLogin from "../pages/PageLogin.vue"; // Import the login page component
import PageRegister from "../pages/PageRegister.vue"; // Make sure this path is correct

const routes = [
  { path: "/", component: PageHome },
  { path: "/login", component: PageLogin }, // Add login route
  { path: "/register", component: PageRegister }, // Add the register path
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
