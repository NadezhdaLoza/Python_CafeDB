<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>Должности</h2>
      <button class="btn btn-primary" @click="openModal()">Добавить должность</button>
    </div>

    <!-- Универсальная таблица -->
    <GenericTable 
      :items="positions" 
      :columns="[{ key: 'title', label: 'Название должности' }]" 
      id-field="position_id"
      @edit="openModal"
      @delete="handleDelete"
    />

    <!-- Универсальная форма -->
    <GenericForm
      :visible="isModalOpen"
      :title="editItem ? 'Редактирование должности' : 'Новая должность'"
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
  data() {
    return {
      isModalOpen: false,
      editItem: null
    }
  },
  computed: {
    ...mapGetters(['positions'])
  },
  methods: {
    ...mapActions(['fetchPositions', 'addPosition', 'updatePosition', 'deletePosition']),
    
    openModal(item = null) {
      this.editItem = item
      this.isModalOpen = true
    },
    closeModal() {
      this.isModalOpen = false
      this.editItem = null
    },
    
    // Обертка для сохранения, которая игнорирует любые события
    saveItem(payload) {
      // Если payload - это объект события (MouseEvent), игнорируем его полностью
      if (payload && payload.type === 'submit') {
        console.warn("Перехвачено событие submit вместо данных. Игнорирую.");
        return;
      }
      
      // Если payload пустой или не содержит ожидаемых полей, тоже игнорируем
      if (!payload || typeof payload !== 'object' || !('title' in payload)) {
         console.error("Некорректные данные для сохранения:", payload);
         return;
      }

      console.log("Сохраняем данные:", payload);

      this._performSave(payload);
    },

    async _performSave(data) {
      try {
        if (this.editItem) {
          await this.updatePosition({ ...data, id: this.editItem.position_id });
        } else {
          await this.addPosition(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения');
      }
    },

    async handleDelete(id) {
      if (confirm('Вы уверены, что хотите удалить эту запись?')) {
        await this.deletePosition(id);
      }
    }
  },
  created() {
    this.fetchPositions();
  }
}
</script>