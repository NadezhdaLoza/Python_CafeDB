<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Бонусные карты</h2>
      <button class="btn btn-primary" @click="openModal()">Выпустить карту</button>
    </div>
    <GenericTable 
      :items="bonusCards" 
      :columns="[
        { key: 'card_number', label: 'Номер карты' },
        { key: 'balance', label: 'Баланс' },
        { key: 'issue_date', label: 'Дата выпуска' }
      ]" 
      id-field="card_id"
      @edit="openModal"
      @delete="handleDelete"
    />
    <GenericForm
      :visible="isModalOpen"
      title="Бонусная карта"
      :initial-data="editItem"
      :fields="[
        { key: 'card_number', label: 'Номер карты', type: 'text', required: true },
        { key: 'balance', label: 'Начальный баланс', type: 'number', required: false },
        { key: 'issue_date', label: 'Дата выпуска', type: 'date', required: false }
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
  computed: { ...mapGetters(['bonusCards']) },
  methods: {
    ...mapActions(['fetchBonusCards', 'addBonusCard', 'updateBonusCard', 'deleteBonusCard']),
    openModal(item = null) { this.editItem = item; this.isModalOpen = true; },
    closeModal() { this.isModalOpen = false; this.editItem = null; },

    async saveItem(data) {
      if (data && data.type === 'submit') {
        return;
      }
      
      if (!data || !data.card_number) {
        console.error("Нет номера карты в данных:", data);
        return;
      }

      try {
        if (this.editItem) {
          await this.updateBonusCard({ ...data, id: this.editItem.card_id });
        } else {
          await this.addBonusCard(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения');
      }
    },
    async handleDelete(id) { if(confirm('Удалить карту?')) await this.deleteBonusCard(id); }
  },
  created() { this.fetchBonusCards(); }
}
</script>