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
        const response = await axios.post(
          "http://localhost:5000/api/register",
          {
            email: this.email,
            password: this.password,
          },
          { withCredentials: true }
        );

        // Sucesso (201)
        alert(response.data.message);
        this.$router.push("/");
      } catch (e) {
        if (!e.response) {
          alert("Erro de conexão com o servidor.");
          return;
        }

        const status = e.response.status;

        if (status === 400) {
          alert("Campos inválidos: preencha email e senha.");
        } else if (status === 409) {
          alert("E-mail já cadastrado.");
        } else {
          alert("Erro inesperado. Tente novamente.");
        }
      }
    },
  },
};
</script>