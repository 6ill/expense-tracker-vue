import { createRouter, createWebHistory } from 'vue-router'
import Layout from '../views/Layout.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue'
import MainWorkspaceView from '@/views/MainWorkspaceView.vue';
import AddTransactionView from '@/views/AddTransactionView.vue';
import EditTransactionView from '@/views/EditTransactionView.vue';

const routes = [
  {
    path : "/",
    name : Layout,
    children : [
      {
        path: '/',
        name: 'Login',
        component: LoginView,
        beforeEnter: (to, from, next) => {
          if (localStorage.getItem('isAuthenticated') === 'true') {
            next({ name: 'MainWorkspace' }); 
          } else {
            next()
          }
        },
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
        beforeEnter: (to, from, next) => {
          if (localStorage.getItem('isAuthenticated') === 'true') {
            next(); 
          } else {
            next({ name: 'Login' })
          }
        },
      },
      {
        path: '/add-transaction/:category?', 
        name: 'AddTransaction', 
        component: AddTransactionView,
        beforeEnter: (to, from, next) => {
          if (localStorage.getItem('isAuthenticated') === 'true') {
            next(); 
          } else {
            next({ name: 'Login' })
          }
        },
      },
      {
        path: '/edit-transaction/:transactionId', 
        name: 'EditTransaction', 
        component: EditTransactionView,
        beforeEnter: (to, from, next) => {
          if (localStorage.getItem('isAuthenticated') === 'true') {
            next(); 
          } else {
            next({ name: 'Login' })
          }
        },
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
