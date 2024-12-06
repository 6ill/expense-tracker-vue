<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { ref } from 'vue';
const isMenuOpen = ref(false);
</script>
<template>
  <div class="bg-gray-50 text-gray-800">
    <!-- Navbar -->
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

    <!-- Main Content -->
    <RouterView />
  </div>
</template>


<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
