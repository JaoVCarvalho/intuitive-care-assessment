<template>
    <div class="home">
      <h1>Consulta de Operadoras</h1>
  
      <SearchBar @search="handleSearch" />
  
      <OperatorsTable :results="results" />
    </div>
  </template>
  <!-- "@/components/SearchBar.vue" -->
  <script>
  import SearchBar from "../components/SearchBar.vue";
  import OperatorsTable from "../components/OperatorsTable.vue";
  import {
    searchByName,
    searchByAnsCode,
    searchByCnpj,
  } from "../services/api.js";
  
  export default {
    name: "Home",
    components: {
      SearchBar,
      OperatorsTable,
    },
    data() {
      return {
        results: [],
      };
    },
    methods: {
      async handleSearch({ type, query }) {
        let response = [];
  
        if (type === "name") {
          response = await searchByName(query);
        } else if (type === "ans-code") {
          response = await searchByAnsCode(query);
        } else if (type === "cnpj") {
          response = await searchByCnpj(query);
        }
  
        this.results = response;
      },
    },
  };
  </script>
  
  <style scoped>
  .home {
    max-width: 1000px;
    margin: 0 auto;
    padding: 2rem;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 2rem;
  }
  </style>
  