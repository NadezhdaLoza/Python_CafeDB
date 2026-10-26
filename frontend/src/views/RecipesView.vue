<template>
  <div class="container mt-4">
    <h2>Рецепты</h2>
    <button class="btn btn-primary mb-3" @click="openModal()">Добавить ингредиент в блюдо</button>
    
    <GenericTable 
      :items="recipes" 
      :columns="[
        { key: 'dish_name', label: 'Блюдо' },
        { key: 'ingredient_name', label: 'Ингредиент' },
        { key: 'portion_weight', label: 'Вес (г)' } 
      ]" 
      id-field="recipe_id"
      @edit="openModal"
      @delete="handleDelete"
    />

    <GenericForm
      :visible="isModalOpen"
      title="Рецепт"
      :initial-data="editItem"
      :fields="[
        { 
          key: 'dish_id', 
          label: 'Блюдо', 
          type: 'select', 
          required: true,
          options: dishes.map(d => ({ value: d.dish_id, text: d.name }))
        },
        { 
          key: 'ingredient_id', 
          label: 'Ингредиент', 
          type: 'select', 
          required: true,
          options: ingredients.map(i => ({ value: i.ingredient_id, text: i.name })) 
        },
        { key: 'portion_weight', label: 'Вес (г)', type: 'number', required: true, step: 0.001, min: 0  }
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
  computed: { 
    ...mapGetters(['recipes', 'dishes', 'ingredients']) 
  },
  methods: {
    ...mapActions([
      'fetchRecipes', 'fetchDishes', 'fetchIngredients', 
      'addRecipe', 'updateRecipe', 'deleteRecipe'
    ]),
    openModal(item = null) { 
      this.editItem = item ? { ...item } : null; 
      this.isModalOpen = true; 
    },
    closeModal() { 
      this.isModalOpen = false; 
      this.editItem = null; 
    },
    async saveItem(data) {
      if (data && data.type === 'submit') {
        return;
      }
      
      if (!data || !data.dish_id || !data.ingredient_id || data.portion_weight === undefined) {
        alert("Заполните все поля: Блюдо, Ингредиент и Вес");
        return;
      }

      try {
        if (this.editItem) {
          await this.updateRecipe({ ...data, id: this.editItem.recipe_id });
        } else {
          await this.addRecipe(data);
        }
        this.closeModal();
      } catch (e) {
        console.error(e);
        alert('Ошибка сохранения: ' + (e.response?.data?.error || e.message));
      }
    },
    async handleDelete(id) { 
      if(confirm('Удалить запись из рецепта?')) await this.deleteRecipe(id); 
    }
  },
  created() { 
    this.fetchRecipes(); 
    this.fetchDishes(); 
    this.fetchIngredients(); 
  }
}
</script>