<template>
  <div class="logout">
    <h2 v-if="loading">Saindo...</h2>
    <h2 v-else-if="error">{{ error }}</h2>
    <h2 v-else>Você saiu da conta.</h2>

    <router-link to="/">Voltar ao login</router-link>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return { loading: true, error: null };
  },
  async mounted() {
    try {
      await axios.post(
        "http://localhost:5000/api/logout",
        {},
        { withCredentials: true }
      );

      // Logout OK
      this.loading = false;
      this.$router.push("/");

    } catch (e) {
      this.loading = false;

      if (!e.response) {
        this.error = "Erro de conexão com o servidor.";
        return;
      }

      const status = e.response.status;

      if (status === 401) {
        // Sessão já estava expirada → OK, redireciona mesmo assim
        this.$router.push("/");
      } else {
        this.error = "Erro ao fazer logout.";
      }
    }
  },
};
</script>