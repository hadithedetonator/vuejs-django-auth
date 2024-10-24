<template>
  <i :class="`icon-${name}`" :style="{ fontSize: size + 'px' }"></i>
</template>

<script>
export default {
  name: "AtomIcon",
  props: {
    name: {
      type: String,
      required: true,
    },
    size: {
      type: Number,
      default: 24,
    },
  },
};
</script>

<style scoped>
.icon {
  display: inline-block;
}
</style>
