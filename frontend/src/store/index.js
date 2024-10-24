// /router/index.js
import { createRouter, createWebHistory } from "vue-router";
import PageHome from "../pages/PageHome.vue";
import PageLogin from "../pages/PageLogin.vue";
import { useAuthStore } from "../store/authStore";

const routes = [
  { path: "/", component: PageHome },
  { path: "/login", component: PageLogin },
  {
    path: "/dashboard",
    component: () => import("../pages/PageDashboard.vue"),
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore();
      if (!authStore.accessToken) {
        next("/login");
      } else {
        next();
      }
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
