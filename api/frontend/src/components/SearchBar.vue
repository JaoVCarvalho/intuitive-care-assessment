<template>
  <div class="search-bar">
    <select v-model="selectedType">
      <option value="name">Nome</option>
      <option value="ans-code">ANS Code</option>
      <option value="cnpj">CNPJ</option>
    </select>

    <input
      type="text"
      v-model="searchQuery"
      placeholder="Digite sua busca..."
      @keyup.enter="emitSearch"
    />

    <button @click="emitSearch">Buscar</button>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      selectedType: "name",
      searchQuery: "",
    };
  },
  methods: {
    emitSearch() {
      if (!this.searchQuery.trim()) return;
      this.$emit("search", {
        type: this.selectedType,
        query: this.searchQuery.trim(),
      });
    },
  },
};
</script>

<style scoped>
.search-bar {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

input {
  flex: 1;
  padding: 0.4rem;
}

button {
  padding: 0.4rem 1rem;
  cursor: pointer;
}
</style>
