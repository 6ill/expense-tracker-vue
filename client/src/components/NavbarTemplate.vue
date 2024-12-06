<template>
    <nav class="bg-blue-700 shadow-lg">
      <div class="w-full px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo -->
          <div class="flex-shrink-0">
            <RouterLink to="/" class="flex items-center space-x-3">
              <img src="@/assets/logo.svg" alt="Vue Logo" class="h-10 w-10" />
              <span class="text-2xl font-semibold text-white">IBDA Consultation</span>
            </RouterLink>
          </div>
  
          <!-- Links (Hidden on Mobile) -->
          <div class="hidden md:flex space-x-6">
            <RouterLink
              to="/"
              class="text-white hover:text-blue-300 font-medium"
              active-class="text-blue-300"
              exact
            >
              Home
            </RouterLink>
            <RouterLink
              to="/about"
              class="text-white hover:text-blue-300 font-medium"
              active-class="text-blue-300"
            >
              About
            </RouterLink>
            <RouterLink
              to="/example"
              class="text-white hover:text-blue-300 font-medium"
              active-class="text-blue-300"
            >
              Example
            </RouterLink>
          </div>
  
          <!-- Mobile Menu Button -->
          <div class="md:hidden">
            <button
              @click="isMenuOpen = !isMenuOpen"
              class="text-white hover:text-blue-300 focus:outline-none focus:ring-2 focus:ring-white"
              aria-label="Toggle Menu"
            >
              <svg
                class="h-6 w-6"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  :class="{ hidden: isMenuOpen, block: !isMenuOpen }"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16m-7 6h7"
                />
                <path
                  :class="{ block: isMenuOpen, hidden: !isMenuOpen }"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
  
      <!-- Mobile Menu -->
      <div
        v-show="isMenuOpen"
        class="md:hidden bg-blue-600 space-y-2 px-4 py-2 shadow-lg"
      >
        <RouterLink
          to="/"
          class="block text-white hover:text-blue-300 font-medium"
          active-class="text-blue-300"
          exact
        >
          Home
        </RouterLink>
        <RouterLink
          to="/about"
          class="block text-white hover:text-blue-300 font-medium"
          active-class="text-blue-300"
        >
          About
        </RouterLink>
        <RouterLink
          to="/example"
          class="block text-white hover:text-blue-300 font-medium"
          active-class="text-blue-300"
        >
          Example
        </RouterLink>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router';
  import { ref } from 'vue';
  
  const isMenuOpen = ref(false);
  </script>
  
  <style scoped>
  /* Tambahkan gaya untuk navbar */
  </style>