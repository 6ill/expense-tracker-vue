<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-50">
    <div class="bg-white shadow-lg rounded-lg p-8 max-w-md w-full">
      <h1 class="text-2xl font-bold text-center text-blue-700">{{ title }}</h1>
      <p class="text-center text-gray-600 mt-2">{{ description }}</p>

      <form class="mt-6 space-y-4" @submit.prevent="handleLogin">
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            type="email"
            id="email"
            v-model="email"
            placeholder="Enter your email"
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
          {{ submitButtonText }}
        </button>
      </form>

      <div class="flex items-center justify-center mt-6">
        <hr class="w-full border-gray-300" />
        <span class="px-4 text-sm text-gray-600">OR</span>
        <hr class="w-full border-gray-300" />
      </div>

      <div class="flex flex-col mt-6 space-y-4">
        <slot name="social-buttons"></slot>
      </div>

      <div class="mt-6 text-center">
        <slot name="footer-links"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: 'Login'
    },
    description: {
      type: String,
      default: 'Welcome back! Please login to your account.'
    },
    submitButtonText: {
      type: String,
      default: 'Login'
    }
  },
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    handleLogin() {
      // Placeholder for login logic
      if (this.email && this.password) {
        alert(`Logging in with: \nEmail: ${this.email}\nPassword: ${this.password}`);
      } else {
        alert('Please fill in all fields.');
      }
    }
  }
};
</script>
