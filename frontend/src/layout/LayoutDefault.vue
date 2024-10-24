<template>
  <div class="layout-default">
    <OrganismHeader />
    <main>
      <slot />
    </main>
  </div>
</template>

<script>
import OrganismHeader from "../components/organisms/OrganismHeader.vue";

export default {
  name: "LayoutDefault",
  components: {
    OrganismHeader,
  },
};
</script>

<style scoped>
.layout-default {
  display: flex;
  flex-direction: column;
}
main {
  padding: 20px;
}
</style>
