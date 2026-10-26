<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Блюда</h2>
      <button class="btn btn-primary" @click="openModal()">Добавить блюдо</button>
    </div>
    <GenericTable 
      :items="dishes" 
      :columns="[
        { key: 'name', label: 'Название' },
        { key: 'price', label: 'Цена' },
        { key: 'weight', label: 'Вес (г)' },
        { key: 'article_number', label: 'Артикул' },
        { key: 'unit', label: 'Ед. изм.' },
        { key: 'category_title', label: 'Категория' }
      ]" 
      id-field="dish_id"
      @edit="openModal"
      @delete="handleDelete"
    />
    <GenericForm
      :visible="isModalOpen"
      title="Блюдо"
      :initial-data="editItem"
      :fields="[
        { key: 'name', label: 'Название', type: 'text', required: true },
        { key: 'price', label: 'Цена', type: 'number', required: true },
        { key: 'weight', label: 'Вес', type: 'number', required: false },
        { key: 'article_number', label: 'Артикул', type: 'text', required: false },
        { key: 'unit', label: 'Ед. изм.', type: 'text', required: false },
        { 
          key: 'category_id', 
          label: 'Категория', 
          type: 'select', 
          required: false,
          options: categories.map(c => ({ value: c.category_id, text: c.title }))
        }
      ]"
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
  data() { return { isModalOpen: false, editItem: null } },
  computed: { ...mapGetters(['dishes', 'categories']) },
  methods: {
    ...mapActions(['fetchDishes', 'fetchCategories', 'addDish', 'updateDish', 'deleteDish']),
    openModal(item = null) { this.editItem = item ? { ...item } : null; this.isModalOpen = true; },
    closeModal() { this.isModalOpen = false; this.editItem = null; },
    async saveItem(data) {
      if (data && data.type === 'submit') {
        return;
      }

      if (!data || !data.name || !data.name.trim()) {
        alert("Введите название блюда");
        return;
      }

      try {
        if (this.editItem) {
          await this.updateDish({ ...data, id: this.editItem.dish_id });
        } else {
          await this.addDish(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения: ' + (e.response?.data?.error || e.message));
      }
    },
    async handleDelete(id) { if(confirm('Удалить?')) await this.deleteDish(id); }
  },
  created() { 
    this.fetchDishes(); 
    this.fetchCategories(); 
  }
}
</script>