<template>
  <div>
    <h1>{{ pokemon.name }}</h1>
    <!-- Use double curly braces to bind the name -->
    <!-- Add any additional Pokémon details here -->
  </div>
</template>

<script>
export default {
  props: {
    pokemon: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.pokemon-detail {
  display: flex;
  justify-content: center;
}
</style>
