import Vue from "vue";
import Router from "vue-router";
import RegistrationForm from "../components/RegistrationForm.vue";
import LoginForm from "@/components/LoginForm.vue";
import HomePage from "../components/HomePage.vue"; // Import Home component

Vue.use(Router);

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage // Use updated name
  },
  {
    path: "/register",
    name: "Register",
    component: RegistrationForm,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginForm,
  },
];

const router = new Router({
  mode: "history",
  routes,
});

export default router;
