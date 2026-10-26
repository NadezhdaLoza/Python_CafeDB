<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Поставщики</h2>
      <button class="btn btn-primary" @click="openModal()">Добавить поставщика</button>
    </div>
    <GenericTable 
      :items="suppliers" 
      :columns="[
        { key: 'company_name', label: 'Компания' },
        { key: 'manager_full_name', label: 'Менеджер' },
        { key: 'phone', label: 'Телефон' }
      ]" 
      id-field="supplier_id"
      @edit="openModal"
      @delete="handleDelete"
    />
    <GenericForm
      :visible="isModalOpen"
      title="Поставщик"
      :initial-data="editItem"
      :fields="[
        { key: 'company_name', label: 'Название компании', type: 'text', required: true },
        { key: 'manager_full_name', label: 'ФИО менеджера', type: 'text', required: false },
        { key: 'phone', label: 'Телефон', type: 'text', required: false }
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
  computed: { ...mapGetters(['suppliers']) },
  methods: {
    ...mapActions(['fetchSuppliers', 'addSupplier', 'updateSupplier', 'deleteSupplier']),
    openModal(item = null) { this.editItem = item; this.isModalOpen = true; },
    closeModal() { this.isModalOpen = false; this.editItem = null; },
    async saveItem(data) {
      console.log("Данные от поставщика:", data); 
      if (data && data.type === 'submit') {
        return;
      }

      if (!data || !data.company_name || !data.company_name.trim()) {
        alert("Введите название поставщика");
        return;
      }

      try {
        if (this.editItem) {
          await this.updateSupplier({ ...data, id: this.editItem.supplier_id });
        } else {
          await this.addSupplier(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения: ' + (e.response?.data?.error || e.message));
      }
    },
    async handleDelete(id) { if(confirm('Удалить?')) await this.deleteSupplier(id); }
  },
  created() { this.fetchSuppliers(); }
}
</script>