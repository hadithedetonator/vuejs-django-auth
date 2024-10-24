<template>
    <LayoutDefault>
      <TemplatePokemonList />
    </LayoutDefault>
  </template>
  
  <script>
  import LayoutDefault from '../layout/LayoutDefault.vue';
  import TemplatePokemonList from '../components/templates/TemplatePokemonList.vue';
  
  export default {
    name: 'PageHome',
    components: {
      LayoutDefault,
      TemplatePokemonList
    }
  };
  </script>
  