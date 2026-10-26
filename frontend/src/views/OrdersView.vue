<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Заказы (товарные чеки)</h2>
      <button class="btn btn-primary" @click="openOrderModal()">Новый заказ (товарный чек)</button>
    </div>

    <!-- Список заказов -->
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>№ Заказа (товарного чека)</th>
          <th>Дата</th>
          <th>Клиент</th>
          <th>Сумма</th>
          <th>Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.order_id" @dblclick="handleDoubleClick(order)" style="cursor: pointer;">
          <td>{{ order.order_number }}</td>
          <td>{{ order.order_date }}</td>
          <td>{{ getClientName(order.client_id) }}</td>
          <td>{{ order.total_amount }} руб.</td>
          <td>
            <button class="btn btn-sm btn-warning me-2" @click="openOrderModal(order)">&#9998;</button>
            <button class="btn btn-sm btn-danger" @click="handleDelete(order.order_id)">&#128465;</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Специальная форма для заказа -->
    <OrderForm
      :visible="isOrderModalOpen"
      :initial-data="currentOrder"
      :employees="employees"
      :clients="clients"
      :dishes="dishes"
      @submit="saveOrder"
      @cancel="closeOrderModal"
    />
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import OrderForm from '@/components/OrderForm.vue'

export default {
  components: { OrderForm },
  data() {
    return {
      isOrderModalOpen: false,
      currentOrder: null
    }
  },
  computed: {
    ...mapGetters(['orders', 'employees', 'clients', 'dishes'])
  },
  methods: {
    ...mapActions([
      'fetchOrders', 
      'fetchEmployees', 
      'fetchClients', 
      'fetchDishes', 
      'addOrder', 
      'updateOrder', 
      'deleteOrder'
    ]),
    

    getClientName(id) {
      const client = this.clients.find(c => c.client_id === id)
      if (!client) return 'Неизвестно';
      return client.full_name || `${client.last_name} ${client.first_name}`;
    },

    handleDoubleClick(order) {
      this.$router.push({ name: 'OrderDetail', params: { id: order.order_id } })
    },

    async openOrderModal(order = null, mode = 'edit') {
      this.modalMode = 'edit'     
      this.isOrderModalOpen = true;
      
      if (order) {
        try {
          const fullOrder = await this.$store.dispatch('fetchOrderById', order.order_id);
          this.currentOrder = fullOrder;
        } catch (e) {
          console.error("Не удалось загрузить детали заказа", e);
          alert("Ошибка загрузки данных заказа");
          this.closeOrderModal();
        }
      } else {
        this.currentOrder = null;
      }
    },
    
    closeOrderModal() {
      this.isOrderModalOpen = false;
      this.currentOrder = null;
    },

    async saveOrder(data) {
      if (data && data.type === 'submit') {
        return;
      }
      
      if (!data || !data.order_number) {
        alert("Номер заказа обязателен!");
        return;
      }

      console.log("Сохранение заказа:", data);

      try {
        if (this.currentOrder) {
          await this.updateOrder({ ...data, id: this.currentOrder.order_id });
        } else {
          await this.addOrder(data);
        }
        this.closeOrderModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения заказа: ' + (e.response?.data?.error || e.message));
      }
    },

    async handleDelete(id) {
      if (confirm('Вы уверены, что хотите удалить этот заказ?')) {
        try {
          await this.deleteOrder(id);
        } catch (e) {
          alert('Ошибка удаления: ' + (e.response?.data?.error || e.message));
        }
      }
    }
  },
  created() {
    Promise.all([
      this.fetchOrders(),
      this.fetchEmployees(),
      this.fetchClients(),
      this.fetchDishes()
    ])
  }
}
</script>