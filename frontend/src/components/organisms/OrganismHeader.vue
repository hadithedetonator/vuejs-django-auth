<template>
  <header
    class="flex justify-between items-center p-4 bg-gray-100 border-b border-gray-300"
  >
    <div class="text-xl font-bold">
      <h1>My App</h1>
    </div>
    <nav>
      <ul class="flex space-x-6">
        <li>
          <router-link to="/" class="text-gray-700 hover:text-blue-600"
            >Home</router-link
          >
        </li>
        <li>
          <router-link to="/about" class="text-gray-700 hover:text-blue-600"
            >About</router-link
          >
        </li>
        <li>
          <router-link to="/contact" class="text-gray-700 hover:text-blue-600"
            >Contact</router-link
          >
        </li>
      </ul>
    </nav>
    <div class="relative">
      <button
        @click="toggleProfileMenu"
        class="text-gray-700 hover:text-blue-600"
      >
        Profile
      </button>
      <div
        v-if="isProfileMenuOpen"
        class="absolute right-0 mt-2 w-48 bg-white border border-gray-300 shadow-lg"
      >
        <ul class="py-2">
          <li>
            <router-link
              to="/profile"
              class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
              >My Profile</router-link
            >
          </li>
          <li
            @click="logout"
            class="block px-4 py-2 text-gray-700 hover:bg-gray-100 cursor-pointer"
          >
            Logout
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "OrganismHeader",
  data() {
    return {
      isProfileMenuOpen: false,
    };
  },
  methods: {
    toggleProfileMenu() {
      this.isProfileMenuOpen = !this.isProfileMenuOpen;
    },
    logout() {
      // Implement logout logic here
      console.log("User logged out");
    },
  },
};
</script>

<style scoped>
/* Add any additional custom styles here */
</style>
