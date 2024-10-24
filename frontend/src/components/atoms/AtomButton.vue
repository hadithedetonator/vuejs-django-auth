<template>
  <button>{{ label }}</button>
</template>

<script>
export default {
  name: "AtomButton",
  props: {
    label: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
/* Add styles for AtomButton */
</style>
