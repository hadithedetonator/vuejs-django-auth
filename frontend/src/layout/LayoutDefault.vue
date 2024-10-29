<template>
  <div class="layout-default">
    <OrganismHeader />
    <SideBar />
    <main>
      <slot />
    </main>
  </div>
</template>

<script>
import OrganismHeader from "@/components/organisms/OrganismHeader.vue";
import SideBar from "@/components/molecules/SideBar.vue";
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
