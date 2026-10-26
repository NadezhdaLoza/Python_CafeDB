<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Клиенты</h2>
      <button class="btn btn-primary" @click="openModal()">Добавить клиента</button>
    </div>
    <GenericTable 
      class="wide-name-col"
      :items="clients" 
      :columns="[
        { key: 'full_name', label: 'ФИО' },
        { key: 'phone', label: 'Телефон' },
        { key: 'card_number', label: 'Карта лояльности' }
      ]" 
      id-field="client_id"
      @edit="openModal"
      @delete="handleDelete"
    />
    <GenericForm
      :visible="isModalOpen"
      title="Клиент"
      :initial-data="editItem"
      :fields="[
        { key: 'last_name', label: 'Фамилия', type: 'text', required: true },
        { key: 'first_name', label: 'Имя', type: 'text', required: true },
        { key: 'middle_name', label: 'Отчество', type: 'text', required: false },
        { key: 'phone', label: 'Телефон', type: 'text', required: false },
        { 
          key: 'card_id', 
          label: 'Бонусная карта', 
          type: 'select', 
          required: false,
          options: bonusCards.map(b => ({ value: b.card_id, text: b.card_number + ' (' + b.balance + ' б.)' }))
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
  computed: { ...mapGetters(['clients', 'bonusCards']) },
  methods: {
    ...mapActions(['fetchClients', 'fetchBonusCards', 'addClient', 'updateClient', 'deleteClient']),
    openModal(item = null) { this.editItem = item; this.isModalOpen = true; },
    closeModal() { this.isModalOpen = false; this.editItem = null; },
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
          await this.updateClient({ ...data, id: this.editItem.client_id });
        } else {
          await this.addClient(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения: ' + (e.response?.data?.error || e.message));
      }
    },
    async handleDelete(id) { if(confirm('Удалить клиента?')) await this.deleteClient(id); }
  },
  created() { 
    this.fetchClients(); 
    this.fetchBonusCards(); 
  }
}
</script>

<style>
  .wide-name-col table th:first-child,
  .wide-name-col table td:first-child {
    
    min-width: 1000px;
  }
</style>