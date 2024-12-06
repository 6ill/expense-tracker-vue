<template>
  <RegisterTemplate
    :title="'Register'"
    :description="'Create a new account.'"
    :submitButtonText="'Register'"
    @submit="handleRegister"
  >
    <template #footer-links>
      <p class="text-sm text-gray-600">
        Already have an account?
        <a href="/login" class="text-blue-600 hover:underline">Login</a>
      </p>
    </template>
  </RegisterTemplate>
</template>

<script>
import RegisterTemplate from '@/components/RegisterTemplate.vue';
import apiClient from '../../apiClient';

export default {
  components: {
    RegisterTemplate,
  },
  methods: {
    async handleRegister({ username, password }) {
      try {
        console.log({ username });
        console.log({ password });
        const response = await apiClient.post('/users/register', { username, password });
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
