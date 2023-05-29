import { createRouter, createWebHistory } from 'vue-router';
import FrontPage from '../components/FrontPage.vue';

const routes = [
  {
    path: '/',
    name: 'FrontPage',
    component: FrontPage
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;