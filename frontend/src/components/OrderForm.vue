<template>
  <transition name="modal">
    <div class="modal-mask" v-if="visible">
      <div class="modal-wrapper modal-lg">
        <div class="modal-container">
          <div class="modal-header">
            <h3>{{ editing ? 'Редактирование заказа (товарного чека)' : 'Новый заказ (товарный чек)' }}</h3>
            <button class="modal-close" @click="$emit('cancel')">&times;</button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="handleSubmit">
              <div class="row mb-3">
                <div class="col-md-6">
                  <label class="form-label">Номер заказа (товарного чека)</label>
                  <input type="number" class="form-control" v-model.number="form.order_number" required>
                </div>
                <div class="col-md-6">
                  <label class="form-label">Дата</label>
                  <input type="date" class="form-control" v-model="form.order_date" required>
                </div>
              </div>
              
              <div class="row mb-3">
                <div class="col-md-6">
                  <label class="form-label">Сотрудник</label>
                  <select class="form-select" v-model.number="form.employee_id" required>
                    <option v-for="emp in employees" :key="emp.employee_id" :value="emp.employee_id">
                      {{ emp.full_name }}
                    </option>
                  </select>
                </div>
                <div class="col-md-6">
                  <label class="form-label">Клиент</label>
                  <select class="form-select" v-model.number="form.client_id" required>
                    <option v-for="client in clients" :key="client.client_id" :value="client.client_id">
                      {{ client.full_name }}
                    </option>
                  </select>
                </div>
              </div>

              <h4 class="mt-4">Состав заказа (товарного чека)</h4>
              <table class="table table-bordered">
                <thead>
                  <tr>
                    <th>Блюдо</th>
                    <th>Цена</th>
                    <th>Кол-во</th>
                    <th>Артикул</th>
                    <th>Ед. изм.</th>
                    <th>Сумма</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in form.items" :key="index">
                    <td>
                      <select class="form-select" v-model.number="item.dish_id" @change="updateItemPrice(index)" required>
                        <option v-for="dish in dishes" :key="dish.dish_id" :value="dish.dish_id">
                          {{ dish.name }}
                        </option>
                      </select>
                    </td>
                    <td><input type="number" class="form-control" v-model.number="item.price"></td>
                    <td><input type="number" class="form-control" v-model.number="item.quantity" min="1" @input="calcTotal(index)" required></td>
                    <td><input type="text" class="form-control" v-model="item.article_number" readonly></td>
                    <td><input type="text" class="form-control" v-model="item.unit" readonly></td>
                    <td>{{ item.total_amount }}</td>
                    <td><button type="button" class="btn btn-danger btn-sm" @click="removeItem(index)">×</button></td>
                  </tr>
                </tbody>
              </table>
              <button type="button" class="btn btn-primary btn-sm" @click="addItem">+ Добавить блюдо</button>

              <div class="mt-3 text-end">
                <h4>Итого: {{ totalOrderAmount }}</h4>
              </div>

              <div class="modal-footer">
                <button type="submit" class="btn btn-success">Сохранить</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    visible: Boolean,
    initialData: Object,
    employees: Array,
    clients: Array,
    dishes: Array
  },
  data() {
    return {
      form: {
        order_number: '',
        employee_id: null,
        client_id: null,
        order_date: '',
        order_time: '12:00:00',
        total_amount: 0,
        items: []
      }
    }
  },
  computed: {
    editing() { return !!this.initialData },
    totalOrderAmount() {
      return this.form.items.reduce((sum, item) => sum + (item.total_amount || 0), 0)
    }
  },
  watch: {
    initialData: {
      immediate: true,
      handler(val) {
        if (val) {
          this.form = JSON.parse(JSON.stringify(val))
          if (!this.form.items) this.form.items = []
        } else {
          this.resetForm()
        }
      }
    }
  },
  methods: {
    resetForm() {
      const now = new Date();
      const simpleNumber = Math.floor(now.getTime() / 1000);
      
      this.form = {
        order_number: simpleNumber, 
        employee_id: null,
        client_id: null,
        order_date: new Date().toISOString().split('T')[0],
        order_time: '12:00:00',
        total_amount: 0,
        items: []
      }
    },
    addItem() {
      this.form.items.push({ dish_id: null, quantity: 1, price: 0, total_amount: 0, article_number: '', unit: '' })
    },
    removeItem(index) {
      this.form.items.splice(index, 1)
      this.calcTotalAll()
    },
    updateItemPrice(index) {
      const dish = this.dishes.find(d => d.dish_id === this.form.items[index].dish_id)
      if (dish) {
        this.form.items[index].price = dish.price
        this.form.items[index].article_number = dish.article_number || ''
        this.form.items[index].unit = dish.unit || ''        
        this.calcTotal(index)
      }
    },
    calcTotal(index) {
      const item = this.form.items[index]
      item.total_amount = item.price * item.quantity
      this.calcTotalAll()
    },
    calcTotalAll() {
      this.form.total_amount = this.totalOrderAmount
    },
    handleSubmit() {
      this.form.total_amount = this.totalOrderAmount;
      
      if (!this.form.order_number) {
        alert("Пожалуйста, введите номер заказа!");
        return;
      }
      const cleanItems = this.form.items.map(item => ({
        dish_id: item.dish_id,
        quantity: item.quantity,
        price: item.price,
        total_amount: item.total_amount
      }));

      const payload = { ...this.form, items: cleanItems };

      console.log("Отправляем заказ:", this.form);
      this.$emit('submit', { ...this.form });
    }
  }
}
</script>

<style scoped>
.modal-lg { max-width: 800px; }
.modal-mask { position: fixed; z-index: 9998; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.5); display: flex; justify-content: center; align-items: center; }
.modal-wrapper { width: 100%; padding: 20px; }
.modal-container { background-color: #fff; border-radius: 8px; padding: 20px; }
.modal-header { display: flex; justify-content: space-between; margin-bottom: 20px; }
</style>