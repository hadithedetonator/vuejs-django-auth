import { createRouter, createWebHistory } from "vue-router";
import LoginPage from "@/pages/LoginPage.vue";
import ServicesPage from "@/pages/ServicesPage.vue";
import SignUpPage from "@/pages/SignUpPage.vue";

const routes = [
  { path: "/login", component: LoginPage },
  { path: "/services", component: ServicesPage },
  { path: "/signup", component: SignUpPage },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
