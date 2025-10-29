import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('@/layouts/MainLayout.vue'), 
      children: [
        {
          path: '',
          name: 'home',
          component: () => import('@/views/HomeView.vue'),
        },
        {
          path: '/new/:id',
          name: 'new',
          component: () => import('@/views/NewView.vue'),
        },
        {
          path: '/news',
          name: 'news',
          component: () => import('@/views/NewsView.vue'),
        }
      ],
    }
  ],
  scrollBehavior(to, from, savedPosition) {
  if (savedPosition) {
    return savedPosition;
  } else {
    return { top: 0 };
  }
}
});

export default router;
