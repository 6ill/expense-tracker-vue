import { createRouter, createWebHistory } from 'vue-router'
import Layout from '../views/Layout.vue';
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue';
import ExamplePage from '../views/example.vue';

const routes = [
  {
    path : "/",
    name : Layout,
    children : [
      {
        path: '/',
        name: 'login',
        component: LoginView,
      },
      {
        path: '/about',
        name: 'about',
        component: () => import('../views/AboutView.vue'),
      },
      {
        path: '/example', // Define the new route
        name: 'Example',
        component: ExamplePage,
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
