<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-50">
    <div class="bg-white shadow-lg rounded-lg p-8 max-w-md w-full">
      <h1 class="text-2xl font-bold text-center text-blue-700">{{ title }}</h1>
      <p class="text-center text-gray-600 mt-2">{{ description }}</p>

      <form class="mt-6 space-y-4" @submit.prevent="submitForm">
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
          {{ submitButtonText }}
        </button>
      </form>

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
      default: 'Register',
    },
    description: {
      type: String,
      default: 'Create a new account.',
    },
    submitButtonText: {
      type: String,
      default: 'Register',
    },
  },
  data() {
  return {
    username: '',
    password: '',
    isSubmitting: false, 
  };
},
methods: {
  submitForm() {
    if (this.isSubmitting) {
      console.log('submitForm already in progress');
      return;
    }
    this.isSubmitting = true;
    console.log('submitForm called');
    this.$emit('submit', { username: this.username, password: this.password });
    this.isSubmitting = false;
  },
},

};
</script>

<style scoped>
</style>
  
  <style scoped>
  /* Tambahkan gaya untuk register container */
  </style>
