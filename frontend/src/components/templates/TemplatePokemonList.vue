<template>
  <div class="pokemon-list">
    <MoleculeSearchInput @search="searchPokemon" />
    <div v-if="pokemons.length">
      <MoleculePokemonThumbnail
        v-for="pokemon in filteredPokemons"
        :key="pokemon.id"
        :pokemon="pokemon"
        @click="selectPokemon(pokemon)"
      />
    </div>
    <p v-else>No pokemons found.</p>
  </div>
</template>

<script>
import { usePokemonStore } from "../../store/pokemonStore";
import MoleculeSearchInput from "../molecules/MoleculeSearchInput.vue";
import MoleculePokemonThumbnail from "../molecules/MoleculePokemonThumbnail.vue";

export default {
  name: "TemplatePokemonList",
  components: {
    MoleculeSearchInput,
    MoleculePokemonThumbnail,
  },
  setup() {
    const pokemonStore = usePokemonStore();

    // Fetch Pokémon data when component is mounted
    pokemonStore.fetchPokemons();

    return {
      pokemons: pokemonStore.pokemonList,
      selectPokemon: pokemonStore.selectPokemon,
    };
  },
  data() {
    return {
      searchQuery: "",
    };
  },
  computed: {
    filteredPokemons() {
      return this.pokemons.filter((pokemon) =>
        pokemon.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
  methods: {
    searchPokemon(query) {
      this.searchQuery = query;
    },
  },
};
</script>
