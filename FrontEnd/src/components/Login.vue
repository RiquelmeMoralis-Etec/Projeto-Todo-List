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
        const res = await axios.post(
          "http://localhost:5000/api/login",
          {
            email: this.email,
            password: this.password,
          },
          { withCredentials: true }
        );

        // Sucesso
        this.$router.push("/dashboard");

      } catch (e) {
        if (!e.response) {
          alert("Erro de conexão com o servidor.");
          return;
        }

        const status = e.response.status;

        if (status === 400) {
          alert("Preencha email e senha.");
        } else if (status === 401) {
          alert("E-mail ou senha incorretos.");
        } else {
          alert("Erro inesperado. Tente novamente.");
        }
      }
    },
  },
};
</script>