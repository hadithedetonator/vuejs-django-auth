import { defineStore } from "pinia";

export const usePokemonStore = defineStore("pokemon", {
  state: () => ({
    pokemons: [],
    selectedPokemon: null,
  }),
  actions: {
    async fetchPokemons() {
      // Simulate an API call to fetch Pokémon data
      this.pokemons = [
        {
          id: 1,
          name: "Pikachu",
          image: "/assets/images/pikachu.png",
          description: "Electric type",
        },
        {
          id: 2,
          name: "Charmander",
          image: "/assets/images/charmander.png",
          description: "Fire type",
        },
      ];
    },
    selectPokemon(pokemon) {
      this.selectedPokemon = pokemon;
    },
  },
  getters: {
    pokemonList: (state) => state.pokemons,
    pokemonById: (state) => (id) =>
      state.pokemons.find((pokemon) => pokemon.id === id),
  },
});
