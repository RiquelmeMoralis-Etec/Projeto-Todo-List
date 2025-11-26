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
  let logged = false;
  try {
    const r = await api.get("/session", { withCredentials: true });
    if (r.status === 200) logged = true;
  } catch (e) {
    logged = false;
  }
  if ((to.path === "/login" || to.path === "/register") && logged) {
    return next("/dashboard");
  }
  if (to.meta.requiresAuth && !logged) {
    return next("/login");
  }
  next();
});

export default router;