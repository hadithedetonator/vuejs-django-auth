<template>
  <LayoutDefault>
    <SideBar />
    <router-view />
  </LayoutDefault>
</template>

<script>
import SideBar from "./components/molecules/SideBar.vue";
export default {
  components: {
    SideBar,
  },
};
</script>
