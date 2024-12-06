<template>
  <LoginTemplate
    :title="'Login'"
    :description="'Welcome back! Please login to your account.'"
    :submitButtonText="'Login'"
  >
    <template #social-buttons>
      <!-- Social Login Buttons -->
      <button
        type="button"
        class="flex items-center justify-center w-full bg-gray-100 text-gray-700 font-bold py-2 px-4 rounded-lg shadow hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-300"
      >
        <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
          <path d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.406.593 24 1.325 24h11.495v-9.294H9.645v-3.622h3.175V8.406c0-3.152 1.922-4.866 4.732-4.866 1.345 0 2.502.099 2.839.144v3.287h-1.948c-1.528 0-1.824.727-1.824 1.791v2.348h3.64l-.475 3.622h-3.165V24h6.218c.729 0 1.324-.593 1.324-1.324V1.325C24 .593 23.406 0 22.675 0z" />
        </svg>
        Continue with Facebook
      </button>
      <button
        type="button"
        class="flex items-center justify-center w-full bg-white border border-gray-300 text-gray-700 font-bold py-2 px-4 rounded-lg shadow hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-300"
      >
        <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 2C6.477 2 2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.988h-2.54V12H10.44v-1.992c0-2.51 1.492-3.897 3.777-3.897 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.631.774-1.631 1.566V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12c0-5.523-4.477-10-10-10z" />
        </svg>
        Continue with Google
      </button>
    </template>

    <template #footer-links>
      <!-- Footer Links -->
      <p class="text-sm text-gray-600">
        Don't have an account? 
        <a href="/signup" class="text-blue-600 hover:underline">Sign up</a>
      </p>
      <p class="text-sm text-gray-600 mt-2">
        Forgot your password? 
        <a href="/reset-password" class="text-blue-600 hover:underline">Reset here</a>
      </p>
    </template>
  </LoginTemplate>
</template>

<script>
import LoginTemplate from '@/components/LoginTemplate.vue';

export default {
  components: {
    LoginTemplate
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

<style>
body {
  font-family: 'Arial', sans-serif;
}
</style>