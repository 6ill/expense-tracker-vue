<template>
  <div id="app">
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from '@/components/NavbarTemplate.vue';

export default {
  name: 'App',
  components: {
    Navbar
  }
};
</script>

<style>
body {
  font-family: 'Arial', sans-serif;
  background-color: #f0f4f8;
  margin: 0;
  padding: 0;
  min-height: 100vh;
}
</style>