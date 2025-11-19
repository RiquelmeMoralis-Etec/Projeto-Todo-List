<template>
  <div class="auth-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <input type="email" v-model="email" placeholder="E-mail" required />
      <input type="password" v-model="password" placeholder="Senha" required />
      <button type="submit">Entrar</button>
    </form>
    <p>
      Não tem conta?
      <router-link to="/register">Cadastre-se</router-link>
    </p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return { email: "", password: "" };
  },
  methods: {
    async handleLogin() {
      try {
        const res = await axios.post("http://localhost:5000/api/login", {
          email: this.email,
          password: this.password,
        },{ withCredentials: true });
        this.$router.push("/dashboard");
      } catch (e) {
        alert("E-mail ou senha incorretos.");
      }
    },
  },
};
</script>