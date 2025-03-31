<template>
  <div class="table-wrapper">
    <div class="scroll-area" v-if="paginatedResults.length">
      <table>
        <thead>
          <tr>
            <th>ANS Code</th>
            <th>CNPJ</th>
            <th>Razão Social</th>
            <th>Nome Fantasia</th>
            <th>Modalidade</th>
            <th>Cidade</th>
            <th>Estado</th>
            <th>Email</th>
            <th>Data Registro</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(operator, index) in paginatedResults" :key="index">
            <td>{{ operator.ans_code }}</td>
            <td>{{ operator.cnpj }}</td>
            <td>{{ operator.corporate_name }}</td>
            <td>{{ operator.trade_name || '-' }}</td>
            <td>{{ operator.modality || '-' }}</td>
            <td>{{ operator.city || '-' }}</td>
            <td>{{ operator.state || '-' }}</td>
            <td>{{ operator.email || '-' }}</td>
            <td>{{ operator.ans_registration_date }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else class="no-results">
      Nenhum resultado encontrado.
    </div>

    <div class="pagination" v-if="totalPages > 1">
      <button :disabled="currentPage === 1" @click="prevPage">Anterior</button>
      <span>Página {{ currentPage }} de {{ totalPages }}</span>
      <button :disabled="currentPage === totalPages" @click="nextPage">Próxima</button>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: "OperatorsTable",
    props: {
      results: {
        type: Array,
        required: true,
      },
      perPage: {
        type: Number,
        default: 10,
      },
    },
    data() {
      return {
        currentPage: 1,
      };
    },
    computed: {
      totalPages() {
        return Math.ceil(this.results.length / this.perPage);
      },
      paginatedResults() {
        const start = (this.currentPage - 1) * this.perPage;
        return this.results.slice(start, start + this.perPage);
      },
    },
    methods: {
      nextPage() {
        if (this.currentPage < this.totalPages) this.currentPage++;
      },
      prevPage() {
        if (this.currentPage > 1) this.currentPage--;
      },
    },
    watch: {
      results() {
        this.currentPage = 1; 
      },
    },
  };
  </script>
  
  <style scoped>
  .table-wrapper {
    position: relative;
    margin-top: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .scroll-area {
    width: 100%;
    overflow-x: auto;
    margin-bottom: 1rem; 
  }
  
  table {
    min-width: 900px;
    width: 100%;
    border-collapse: collapse;
  }
  
  th,
  td {
    border: 1px solid #ccc;
    padding: 0.5rem;
    text-align: left;
    white-space: nowrap;
  }
  
  th {
    background-color: #f4f4f4;
  }
  
  .no-results {
    margin: 1rem 0;
    color: #888;
  }
  
  .pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    background-color: #f8f9fa;
    padding: 0.5rem;
    width: 100%;
    position: sticky;
    bottom: 0;
    z-index: 10;
  }
  
  button[disabled] {
    opacity: 0.5;
    cursor: not-allowed;
  }
  </style>
  