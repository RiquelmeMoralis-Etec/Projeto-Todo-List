import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import AppDashboard from "../AppDashboard.vue";
import api from "../services/api";
import Register from "../components/Register.vue";

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", component: Login },
  { path: "/register", component: Register},
  { path: "/dashboard", component: AppDashboard, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  if (!to.meta.requiresAuth) return next();

  try {
    const response = await api.get("/session", { withCredentials: true });

    // deve tratar a resposta com o código HTTP correspondente, e não utilizando o campo 'data'.
    if (response.data.logged_in) next();
    else next("/login");
  } catch (err) {
    next("/login");
  }
});

export default router;