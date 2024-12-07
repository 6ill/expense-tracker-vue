import { createRouter, createWebHistory } from 'vue-router'
import Layout from '../views/Layout.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue'
import MainWorkspaceView from '@/views/MainWorkspaceView.vue';

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
        path: '/register',
        name: 'Register',
        component: RegisterView,
      },
      {
        path: '/main-workspace',
        name: 'MainWorkspace',
        component: MainWorkspaceView,
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
