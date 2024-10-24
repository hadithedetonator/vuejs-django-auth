<template>
  <div>
    <h3>{{ pokemon.name }}</h3>
    <img :src="pokemon.image" alt="pokemon.name" />
  </div>
</template>

<script>
export default {
  name: "MoleculePokemonThumbnail",
  props: {
    pokemon: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
/* Add styles for MoleculePokemonThumbnail */
</style>
