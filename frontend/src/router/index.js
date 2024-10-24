import { createRouter, createWebHistory } from "vue-router";
import PageHome from "../pages/PageHome.vue";
import PagePokemonDetail from "../pages/PagePokemonDetail.vue";

const routes = [
  { path: "/", component: PageHome },
  { path: "/pokemon/:id", component: PagePokemonDetail },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
