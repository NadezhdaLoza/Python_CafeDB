import { createStore } from 'vuex'
import axios from 'axios'

const api = axios.create({
  baseURL: "http://localhost:5000/api/",
  timeout: 5000
})

export default createStore({
  state: {
    positions: [],
    categories: [],
    suppliers: [],
    ingredients: [],
    dishes: [],
    recipes: [],
    bonusCards: [],
    employees: [],
    clients: [],
    orders: [],
    currentOrder: null,
    isLoading: false
  },
  mutations: {
    SET_POSITIONS(state, data) { state.positions = data },
    SET_CATEGORIES(state, data) { state.categories = data },
    SET_SUPPLIERS(state, data) { state.suppliers = data },
    SET_INGREDIENTS(state, data) { state.ingredients = data },
    SET_DISHES(state, data) { state.dishes = data },
    SET_RECIPES(state, data) { state.recipes = data },
    SET_BONUS_CARDS(state, data) { state.bonusCards = data },
    SET_EMPLOYEES(state, data) { state.employees = data },
    SET_CLIENTS(state, data) { state.clients = data },
    SET_ORDERS(state, data) { state.orders = data },
    SET_CURRENT_ORDER(state, data) { state.currentOrder = data },
    SET_LOADING(state, status) { state.isLoading = status }
  },
  actions: {
    async fetchPositions({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/positions/')
        commit('SET_POSITIONS', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addPosition({ dispatch }, item) {
      await api.post('/positions/', item)
      dispatch('fetchPositions')
    },
    async updatePosition({ dispatch }, item) {
      await api.put('/positions/', item)
      dispatch('fetchPositions')
    },
    async deletePosition({ dispatch }, id) {
      await api.delete(`/positions/${id}`)
      dispatch('fetchPositions')
    },

    async fetchCategories({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/categories/')
        commit('SET_CATEGORIES', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addCategory({ dispatch }, item) {
      await api.post('/categories/', item)
      dispatch('fetchCategories')
    },
    async updateCategory({ dispatch }, item) {
      await api.put('/categories/', item)
      dispatch('fetchCategories')
    },
    async deleteCategory({ dispatch }, id) {
      await api.delete(`/categories/${id}`)
      dispatch('fetchCategories')
    },

    async fetchSuppliers({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/suppliers/')
        commit('SET_SUPPLIERS', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addSupplier({ dispatch }, item) {
      await api.post('/suppliers/', item)
      dispatch('fetchSuppliers')
    },
    async updateSupplier({ dispatch }, item) {
      await api.put('/suppliers/', item)
      dispatch('fetchSuppliers')
    },
    async deleteSupplier({ dispatch }, id) {
      await api.delete(`/suppliers/${id}`)
      dispatch('fetchSuppliers')
    },

    async fetchIngredients({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/ingredients/')
        commit('SET_INGREDIENTS', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addIngredient({ dispatch }, item) {
      await api.post('/ingredients/', item)
      dispatch('fetchIngredients')
    },
    async updateIngredient({ dispatch }, item) {
      await api.put('/ingredients/', item)
      dispatch('fetchIngredients')
    },
    async deleteIngredient({ dispatch }, id) {
      await api.delete(`/ingredients/${id}`)
      dispatch('fetchIngredients')
    },

    async fetchDishes({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/dishes/')
        commit('SET_DISHES', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addDish({ dispatch }, item) {
      await api.post('/dishes/', item)
      dispatch('fetchDishes')
    },
    async updateDish({ dispatch }, item) {
      await api.put('/dishes/', item)
      dispatch('fetchDishes')
    },
    async deleteDish({ dispatch }, id) {
      await api.delete(`/dishes/${id}`)
      dispatch('fetchDishes')
    },

    async fetchRecipes({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/recipes/')
        commit('SET_RECIPES', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addRecipe({ dispatch }, item) {
      await api.post('/recipes/', item)
      dispatch('fetchRecipes')
    },
    async deleteRecipe({ dispatch }, id) {
      await api.delete(`/recipes/${id}`)
      dispatch('fetchRecipes')
    },

    async fetchBonusCards({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/bonus-cards/')
        commit('SET_BONUS_CARDS', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addBonusCard({ dispatch }, item) {
      await api.post('/bonus-cards/', item)
      dispatch('fetchBonusCards')
    },
    async updateBonusCard({ dispatch }, item) {
      await api.put('/bonus-cards/', item)
      dispatch('fetchBonusCards')
    },
    async deleteBonusCard({ dispatch }, id) {
      await api.delete(`/bonus-cards/${id}`)
      dispatch('fetchBonusCards')
    },

    async fetchEmployees({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/employees/')
        commit('SET_EMPLOYEES', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addEmployee({ dispatch }, item) {
      await api.post('/employees/', item)
      dispatch('fetchEmployees')
    },
    async updateEmployee({ dispatch }, item) {
      await api.put('/employees/', item)
      dispatch('fetchEmployees')
    },
    async deleteEmployee({ dispatch }, id) {
      await api.delete(`/employees/${id}`)
      dispatch('fetchEmployees')
    },

    async fetchClients({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/clients/')
        commit('SET_CLIENTS', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    async addClient({ dispatch }, item) {
      await api.post('/clients/', item)
      dispatch('fetchClients')
    },
    async updateClient({ dispatch }, item) {
      await api.put('/clients/', item)
      dispatch('fetchClients')
    },
    async deleteClient({ dispatch }, id) {
      await api.delete(`/clients/${id}`)
      dispatch('fetchClients')
    },

    async fetchOrders({ commit }) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get('/orders/')
        commit('SET_ORDERS', res.data)
      } catch (e) { console.error(e) }
      finally { commit('SET_LOADING', false) }
    },
    
    async fetchOrderById({ commit }, id) {
      commit('SET_LOADING', true)
      try {
        const res = await api.get(`/orders/${id}`)
        commit('SET_CURRENT_ORDER', res.data)
        return res.data
      } catch (e) { 
        console.error(e)
        throw e
      }
      finally { commit('SET_LOADING', false) }
    },

    async addOrder({ commit, dispatch }, orderData) {
      commit('SET_LOADING', true)
      try {
        await api.post('/orders/', orderData)
        dispatch('fetchOrders')
      } catch (e) { throw e }
      finally { commit('SET_LOADING', false) }
    },

    async updateOrder({ commit, dispatch }, orderData) {
      commit('SET_LOADING', true)
      try {
        await api.put('/orders/', orderData)
        dispatch('fetchOrders')
      } catch (e) { throw e }
      finally { commit('SET_LOADING', false) }
    },

    async deleteOrder({ commit, dispatch }, id) {
      commit('SET_LOADING', true)
      try {
        await api.delete(`/orders/${id}`)
        dispatch('fetchOrders')
      } catch (e) { throw e }
      finally { commit('SET_LOADING', false) }
    }
  },
  getters: {
    isLoading: state => state.isLoading,
    positions: state => state.positions,
    categories: state => state.categories,
    suppliers: state => state.suppliers,
    ingredients: state => state.ingredients,
    dishes: state => state.dishes,
    recipes: state => state.recipes,
    bonusCards: state => state.bonusCards,
    employees: state => state.employees,
    clients: state => state.clients,
    orders: state => state.orders,
    currentOrder: state => state.currentOrder,

    getPositionById: state => id => state.positions.find(p => p.position_id === id),
    getCategoryById: state => id => state.categories.find(c => c.category_id === id),
    getSupplierById: state => id => state.suppliers.find(s => s.supplier_id === id),
    getIngredientById: state => id => state.ingredients.find(i => i.ingredient_id === id),
    getDishById: state => id => state.dishes.find(d => d.dish_id === id),
    getBonusCardById: state => id => state.bonusCards.find(b => b.card_id === id),
    getEmployeeById: state => id => state.employees.find(e => e.employee_id === id),
    getClientById: state => id => state.clients.find(c => c.client_id === id),
    getOrderById: state => id => state.orders.find(o => o.order_id === id)
  }
})