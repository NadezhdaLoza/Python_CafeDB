<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Категории</h2>
      <button class="btn btn-primary" @click="openModal()">Добавить категорию</button>
    </div>
    <GenericTable 
      :items="categories" 
      :columns="[{ key: 'title', label: 'Название категории' }]" 
      id-field="category_id"
      @edit="openModal"
      @delete="handleDelete"
    />
    <GenericForm
      :visible="isModalOpen"
      :title="editItem ? 'Редактирование категории' : 'Новая категория'"
      :initial-data="editItem"
      :fields="[{ key: 'title', label: 'Название', type: 'text', required: true }]"
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
  computed: { ...mapGetters(['categories']) },
  methods: {
    ...mapActions(['fetchCategories', 'addCategory', 'updateCategory', 'deleteCategory']),
    openModal(item = null) { this.editItem = item; this.isModalOpen = true; },
    closeModal() { this.isModalOpen = false; this.editItem = null; },
    
    async saveItem(data) {
      if (data && data.type === 'submit') {
        return;
      }
      
      if (!data || !data.title || !data.title.trim()) {
        alert("Введите название категории");
        return;
      }

      try {
        if (this.editItem) {
          await this.updateCategory({ ...data, id: this.editItem.category_id });
        } else {
          await this.addCategory(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения: ' + (e.response?.data?.error || e.message));
      }
    },
    async handleDelete(id) { if(confirm('Удалить?')) await this.deleteCategory(id); }
  },
  created() { this.fetchCategories(); }
}
</script>