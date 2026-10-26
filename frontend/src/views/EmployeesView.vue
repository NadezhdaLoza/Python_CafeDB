<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Сотрудники</h2>
      <button class="btn btn-primary" @click="openModal()">Добавить сотрудника</button>
    </div>

    <!-- Таблица -->
    <GenericTable 
      :items="employees" 
      :columns="[
        { key: 'full_name', label: 'ФИО' }, 
        { key: 'phone', label: 'Телефон' },
        { key: 'position_title', label: 'Должность' }
      ]" 
      id-field="employee_id"
      @edit="openModal"
      @delete="handleDelete"
    />

    <!-- Форма с выпадающим списком должностей -->
    <GenericForm
      :visible="isModalOpen"
      title="Сотрудник"
      :initial-data="editItem"
      :fields="employeeFields"
      @submit="saveItem"
      @cancel="closeModal"
    />
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import GenericTable from '@/components/GenericTable.vue'
import GenericForm from '@/components/GenericForm.vue'

export default {
  components: { GenericTable, GenericForm },
  data() {
    return {
      isModalOpen: false,
      editItem: null
    }
  },
  computed: {
    ...mapGetters(['employees', 'positions']),
    // Динамически формируем поля формы
    employeeFields() {
      return [
        { key: 'last_name', label: 'Фамилия', type: 'text', required: true },
        { key: 'first_name', label: 'Имя', type: 'text', required: true },
        { key: 'middle_name', label: 'Отчество', type: 'text', required: false },
        { key: 'phone', label: 'Телефон', type: 'text', required: false },
        { 
          key: 'position_id', 
          label: 'Должность', 
          type: 'select', 
          required: true,
          options: this.positions.map(p => ({ value: p.position_id, text: p.title }))
        }
      ]
    }
  },
  methods: {
    ...mapActions(['fetchEmployees', 'fetchPositions', 'addEmployee', 'updateEmployee', 'deleteEmployee']),
    
    openModal(item = null) {
      this.editItem = item
      this.isModalOpen = true
    },
    closeModal() {
      this.isModalOpen = false
      this.editItem = null
    },
    async saveItem(data) {
      if (data && data.type === 'submit') {
        return;
      }
      
      if (!data || !data.last_name || !data.first_name) {
        alert("Заполните Фамилию и Имя");
        return;
      }

      try {
        if (this.editItem) {
          await this.updateEmployee({ ...data, id: this.editItem.employee_id });
        } else {
          await this.addEmployee(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения: ' + (e.response?.data?.error || e.message));
      }
    },
    async handleDelete(id) {
      if (confirm('Удалить сотрудника?')) {
        await this.deleteEmployee(id)
      }
    }
  },
  created() {
    this.fetchEmployees()
    this.fetchPositions() // Загружаем справочник должностей для select
  }
}
</script>