<template>
  <div class="sidebar">
    <a href="/">
      <img src="./assets/logo.jpg" alt="Logo" class="logo" />
    </a>
    <div v-for="item in menuItems" :key="item.label">
      <AtomButton :label="item.label" @click="toggleSubMenu(item)" />
      <div v-if="item.isOpen" class="sub-buttons">
        <AtomButton
          v-for="subItem in item.subButtons"
          :key="subItem.label"
          :label="subItem.label"
          @click="loadComponent(subItem.component)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import AtomButton from "@/components/atoms/AtomButton.vue"; // Adjust the path as needed

export default {
  name: "SideBar",
  components: {
    AtomButton,
  },
  setup() {
    //Composition API
    const menuItems = ref([
      {
        label: "Dashboard",
        isOpen: false,
        subButtons: [],
      },
      {
        label: "Projects",
        isOpen: false,
        subButtons: [
          { label: "New Project", component: "NewProjectComponent" },
          { label: "Manage Projects", component: "ManageProjectsComponent" },
        ],
      },
      {
        label: "Projects",
        isOpen: false,
        subButtons: [
          { label: "New Project", component: "NewProjectComponent" },
          { label: "Manage Projects", component: "ManageProjectsComponent" },
        ],
      },
    ]);

    const currentComponent = ref(null); // To hold the currently loaded component

    const toggleSubMenu = (item) => {
      item.isOpen = !item.isOpen; // Toggle the visibility of the sub-menu
    };

    const loadComponent = (componentName) => {
      currentComponent.value = componentName; // Load the selected component
    };

    return {
      menuItems,
      currentComponent,
      toggleSubMenu,
      loadComponent,
    };
  },
};
</script>

<style>
.sidebar {
  background-color: #f0f0f0; /* Grey background */
  padding: 20px; /* Add some padding */
  width: 250px; /* Set a width for the sidebar */
  height: 100vh; /* Full height */
  display: flex;
  flex-direction: column; /* Stack buttons vertically */
  gap: 10px; /* Space between buttons */
  border-radius: 50px;
}

.sub-buttons {
  padding-left: 20px; /* Indent sub-buttons */
}
</style>
