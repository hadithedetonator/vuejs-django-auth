<template>
  <div class="search-input">
    <input
      type="text"
      v-model="searchQuery"
      @input="onInput"
      placeholder="Search..."
    />
    <AtomButton label="Search" @click="onSearch" />
  </div>
</template>

<script>
import AtomButton from "../atoms/AtomButton.vue";

export default {
  name: "MoleculeSearchInput",
  components: {
    AtomButton,
  },
  data() {
    return {
      searchQuery: "",
    };
  },
  methods: {
    onInput() {
      this.$emit("input", this.searchQuery);
    },
    onSearch() {
      this.$emit("search", this.searchQuery);
    },
  },
};
</script>

<style scoped>
.search-input {
  display: flex;
}
button {
  color: yellow;
}
</style>
