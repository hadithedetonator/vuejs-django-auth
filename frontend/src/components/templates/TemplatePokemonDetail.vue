<template>
    <div v-if="pokemon" class="pokemon-detail">
      <OrganismPokemonCard :pokemon="pokemon" />
    </div>
  </template>
  
  <script>
  import OrganismPokemonCard from '../organisms/OrganismPokemonCard.vue';
  
  export default {
    name: 'TemplatePokemonDetail',
    components: {
      OrganismPokemonCard
    },
    props: {
      pokemon: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  .pokemon-detail {
    display: flex;
    justify-content: center;
  }
  </style>
  