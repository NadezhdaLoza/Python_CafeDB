<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Ингредиенты</h2>
      <button class="btn btn-primary" @click="openModal()">Добавить ингредиент</button>
    </div>
    <GenericTable 
      :items="ingredients" 
      :columns="[
        { key: 'name', label: 'Название' },
        { key: 'unit', label: 'Ед. изм.' },
        { key: 'supplier_name', label: 'Поставщик' }
      ]" 
      id-field="ingredient_id"
      @edit="openModal"
      @delete="handleDelete"
    />
    <GenericForm
      :visible="isModalOpen"
      title="Ингредиент"
      :initial-data="editItem"
      :fields="[
        { key: 'name', label: 'Название', type: 'text', required: true },
        { key: 'unit', label: 'Единица измерения', type: 'text', required: false },
        { 
          key: 'supplier_id', 
          label: 'Поставщик', 
          type: 'select', 
          required: false,
          options: suppliers.map(s => ({ value: s.supplier_id, text: s.company_name }))
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
  computed: { ...mapGetters(['ingredients', 'suppliers']) },
  methods: {
    ...mapActions(['fetchIngredients', 'fetchSuppliers', 'addIngredient', 'updateIngredient', 'deleteIngredient']),
    openModal(item = null) { this.editItem = item; this.isModalOpen = true; },
    closeModal() { this.isModalOpen = false; this.editItem = null; },
    async saveItem(data) {
      if (data && data.type === 'submit') {
        return;
      }
      
      if (!data || !data.name || !data.name.trim()) {
        alert("Введите название ингредиента");
        return;
      }

      try {
        if (this.editItem) {
          await this.updateIngredient({ ...data, id: this.editItem.ingredient_id });
        } else {
          await this.addIngredient(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения: ' + (e.response?.data?.error || e.message));
      }
    },
    async handleDelete(id) { if(confirm('Удалить?')) await this.deleteIngredient(id); }
  },
  created() { 
    this.fetchIngredients(); 
    this.fetchSuppliers(); 
  }
}
</script>