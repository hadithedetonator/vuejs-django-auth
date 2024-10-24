<template>
  <div class="pokemon-card">
    <h3>{{ pokemon.name }}</h3>
    <img :src="pokemon.image" alt="" />
    <p>{{ pokemon.description }}</p>
  </div>
</template>

<script>
export default {
  name: "OrganismPokemonCard",
  props: {
    pokemon: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.pokemon-card {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 10px;
}
</style>
