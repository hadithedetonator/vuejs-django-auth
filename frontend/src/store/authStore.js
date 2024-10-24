import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    accessToken: null,
    refreshToken: null,
    user: null,
  }),
  actions: {
    async login(payload) {
      try {
        const response = await axios.post(
          "http://localhost:8000/api/login/",
          payload
        );
        this.accessToken = response.data.access;
        this.refreshToken = response.data.refresh;
        this.user = payload.username;
        console.log("Login successful");
      } catch (error) {
        console.error("Error during login", error);
      }
    },

    async register(payload) {
      try {
        const response = await axios.post(
          "http://localhost:8000/api/register/",
          payload
        );
        console.log("User registered successfully:", response.data);
      } catch (error) {
        console.error("Error during registration", error);
      }
    },
  },
});
