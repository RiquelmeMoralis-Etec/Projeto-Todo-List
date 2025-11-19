<template>
  <div class="auth-container">
    <h2>Criar Conta</h2>
    <form @submit.prevent="handleRegister">
      <input type="email" v-model="email" placeholder="E-mail" required />
      <input type="password" v-model="password" placeholder="Senha" required />
      <button type="submit">Cadastrar</button>
    </form>
    <p>
      Já tem conta?
      <router-link to="/">Entrar</router-link>
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
    async handleRegister() {
      try {
        await axios.post("http://localhost:5000/api/register", {
          email: this.email,
          password: this.password,
        });
        alert("Usuário cadastrado com sucesso! Faça login.");
        this.$router.push("/");
      } catch (e) {
        alert("Erro ao cadastrar. E-mail já existente?");
      }
    },
  },
};
</script>