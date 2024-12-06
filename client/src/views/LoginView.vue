<template>
  <LoginTemplate
    :title="'Login'"
    :description="'Welcome back! Please login to your account.'"
    :submitButtonText="'Login'"
  >
    <template #footer-links>
      <!-- Footer Links -->
      <p class="text-sm text-gray-600">
        Don't have an account? 
        <a href="/register" class="text-blue-600 hover:underline">Sign up</a>
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