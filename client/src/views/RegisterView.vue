<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-50">
      <div class="bg-white shadow-lg rounded-lg p-8 max-w-md w-full">
        <h1 class="text-2xl font-bold text-center text-blue-700">Register</h1>
        <p class="text-center text-gray-600 mt-2">Create a new account.</p>
  
        <form class="mt-6 space-y-4" @submit.prevent="handleRegister">
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
            <input
              type="text"
              id="username"
              v-model="username"
              placeholder="Enter your username"
              class="w-full mt-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:outline-none"
              required
            />
          </div>
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <input
              type="password"
              id="password"
              v-model="password"
              placeholder="Enter your password"
              class="w-full mt-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:outline-none"
              required
            />
          </div>
          <button
            type="submit"
            class="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded-lg shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600"
          >
            Register
          </button>
        </form>
  
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600">
            Already have an account?
            <a href="/login" class="text-blue-600 hover:underline">Login</a>
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import apiClient from '../../apiClient';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async handleRegister() {
        try {
          console.log({ username: this.username, password: this.password });
          const response = await apiClient.post('/users/register', {
            username: this.username,
            password: this.password,
          });
          alert(response.data.message);
        } catch (error) {
          console.error('Registration error:', error);
          alert('Registration failed. Please try again.');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #f0f4f8;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>