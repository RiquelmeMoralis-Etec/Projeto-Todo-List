<template>
  <div class="logout">
    <h2>Você saiu da conta.</h2>
    <router-link to="/">Voltar ao login</router-link>
  </div>
</template>

<script>
import axios from "axios";

export default {
  async mounted() {
    await axios.post("http://localhost:5000/api/logout", {}, { withCredentials: true });
    this.$router.push("/");
  },
};
</script>