<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Заказ (товарный чек) № {{ order.order_number }}</h2>
      <div>
        <button class="btn btn-primary me-2" @click="goToEdit">Редактировать</button>
        <router-link to="/orders" class="btn btn-secondary">Назад к списку</router-link>
      </div>
    </div>

    <div v-if="isLoading" class="text-center">Загрузка...</div>
    <div v-else-if="error" class="alert alert-danger">{{ error }}</div>
    
    <div v-else class="card p-4">
        <div class="row mb-4">
            <div class="col-md-6">
                <p><strong>Дата:</strong> {{ order.order_date }}</p>
                <p><strong>Клиент:</strong> {{ getClientName(order.client_id) }}</p>
                <p><strong>Сотрудник:</strong> {{ getEmployeeName(order.employee_id) }}</p>
            </div>
        </div>

        <table class="table table-bordered">
            <thead>
            <tr>
                <th>Блюдо</th>
                <th>Артикул</th>
                <th>Ед. изм.</th>
                <th>Цена</th>
                <th>Кол-во</th>
                <th>Сумма</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in order.items" :key="index">
                <td>{{ item.dish_name }}</td>
                <td>{{ item.article_number || '-' }}</td>
                <td>{{ item.unit || '-' }}</td>
                <td>{{ item.price }}</td>
                <td>{{ item.quantity }}</td>
                <td>{{ item.total_amount }}</td>
            </tr>
            </tbody>
        </table>
        <div class="row mb-4">
            <h4>Итого: {{ order.total_amount }} руб.</h4>
        </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'OrderDetailView',
  data() {
    return {
      isLoading: false,
      error: null,
      order: {}
    }
  },
  computed: {
    ...mapGetters(['clients', 'employees'])
  },
  methods: {
    ...mapActions(['fetchOrderById', 'fetchClients', 'fetchEmployees']),
    
    getClientName(id) {
      const client = this.clients.find(c => c.client_id === id)
      return client ? (client.full_name || `${client.last_name} ${client.first_name}`) : 'Неизвестно'
    },
    
    getEmployeeName(id) {
      const emp = this.employees.find(e => e.employee_id === id)
      return emp ? emp.full_name : 'Неизвестно'
    },

    goToEdit() {
        this.$router.push('/orders')
    }
  },
  async created() {
    this.isLoading = true
    try {
      const orderId = this.$route.params.id
      if (!this.clients || this.clients.length === 0) {
        await this.fetchClients();
      }
      if (!this.employees || this.employees.length === 0) {
        await this.fetchEmployees();
      }
      this.order = await this.fetchOrderById(orderId)
    } catch (e) {
      this.error = 'Ошибка загрузки заказа'
    } finally {
      this.isLoading = false
    }
  }
}
</script>