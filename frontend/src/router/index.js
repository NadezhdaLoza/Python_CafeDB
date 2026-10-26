import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import PositionsView from '../views/PositionsView.vue'
import CategoriesView from '../views/CategoriesView.vue'
import SuppliersView from '../views/SuppliersView.vue'
import IngredientsView from '../views/IngredientsView.vue'
import DishesView from '../views/DishesView.vue'
import RecipesView from '../views/RecipesView.vue'
import BonusCardsView from '../views/BonusCardsView.vue'
import ClientsView from '../views/ClientsView.vue'
import EmployeesView from '../views/EmployeesView.vue'
import OrdersView from '../views/OrdersView.vue'
import OrderDetailView from '@/views/OrderDetailView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/positions',
    name: 'positions',
    component: PositionsView
  },
  {
    path: '/categories',
    name: 'categories',
    component: CategoriesView
  },
  {
    path: '/suppliers',
    name: 'suppliers',
    component: SuppliersView
  },
  {
    path: '/ingredients',
    name: 'ingredients',
    component: IngredientsView
  },
  {
    path: '/dishes',
    name: 'dishes',
    component: DishesView
  },
  {
    path: '/recipes',
    name: 'recipes',
    component: RecipesView
  },
  {
    path: '/bonus-cards',
    name: 'bonus-cards',
    component: BonusCardsView
  },
  {
    path: '/clients',
    name: 'clients',
    component: ClientsView
  },
  {
    path: '/employees',
    name: 'employees',
    component: EmployeesView
  },
  {
    path: '/orders',
    name: 'orders',
    component: OrdersView
  },
  {
    path: '/orders/:id',
    name: 'OrderDetail',
    component: OrderDetailView
  },

  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router