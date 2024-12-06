<template>
    <RegisterTemplate
      :title="'Register'"
      :description="'Create a new account.'"
      :submitButtonText="'Register'"
    >
      <template #footer-links>
        <!-- Footer Links -->
        <p class="text-sm text-gray-600">
          Already have an account? 
          <a href="/login" class="text-blue-600 hover:underline">Login</a>
        </p>
      </template>
    </RegisterTemplate>
  </template>
  
  <script>
  import RegisterTemplate from '@/components/RegisterTemplate.vue';
  
  export default {
    components: {
      RegisterTemplate
    },
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      handleRegister() {
        // Placeholder for register logic
        if (this.username && this.password) {
          alert(`Registering with: \nUsername: ${this.username}\nPassword: ${this.password}`);
        } else {
          alert('Please fill in all fields.');
        }
      }
    }
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