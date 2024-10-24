<template>
  <LayoutDefault>
    <TemplatePokemonDetail :pokemon="pokemon" />
  </LayoutDefault>
</template>

<script>
import { useRoute } from "vue-router"; // Import useRoute to access route parameters
import { usePokemonStore } from "../store/pokemonStore";
import LayoutDefault from "../layout/LayoutDefault.vue";
import TemplatePokemonDetail from "../components/templates/TemplatePokemonDetail.vue";

export default {
  name: "PagePokemonDetail",
  components: {
    LayoutDefault,
    TemplatePokemonDetail,
  },
  setup() {
    const route = useRoute(); // Use useRoute to get the current route
    const pokemonStore = usePokemonStore();
    const id = parseInt(route.params.id); // Access the route parameter for the Pokemon ID
    const pokemon = pokemonStore.pokemonById(id); // Fetch the Pokemon details from the store

    return { pokemon }; // Expose the Pokemon object to the template
  },
};
</script>
