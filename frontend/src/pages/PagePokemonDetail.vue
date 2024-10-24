<template>
    <LayoutDefault>
      <TemplatePokemonDetail :pokemon="pokemon" />
    </LayoutDefault>
  </template>
  
  <script>
  import LayoutDefault from '../layout/LayoutDefault.vue';
  import TemplatePokemonDetail from '../components/templates/TemplatePokemonDetail.vue';
  
  export default {
    name: 'PagePokemonDetail',
    components: {
      LayoutDefault,
      TemplatePokemonDetail
    },
    data() {
      return {
        pokemon: null
      };
    },
    created() {
      const id = this.$route.params.id;
      // Simulate fetching pokemon detail by ID
      this.pokemon = {
        id,
        name: 'Pikachu',
        image: '/assets/images/pikachu.png',
        description: 'Electric type Pokemon.'
      };
    }
  };
  </script>
  