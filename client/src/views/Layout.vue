<template>
    <div>
      <header>
        <nav>
          <router-link to="/">Home</router-link>
          <router-link to="/example">Example</router-link>
        </nav>
      </header>
      <main>
        <router-view /> <!-- Render the current route's component here -->
      </main>
      <footer>
        <p>Footer Content</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: "Layout",
  };
  </script>
  
  <style scoped>
  header {
    background: #4f46e5; /* Tailwind Indigo */
    color: white;
    padding: 10px;
  }
  footer {
    margin-top: 20px;
    text-align: center;
    color: #6b7280; /* Tailwind Gray */
  }
  </style>
  