<template>
  <transition name="modal">
    <div class="modal-mask" v-if="visible">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <h3>{{ title }}</h3>
            <button class="modal-close" @click="$emit('cancel')">&times;</button>
          </div>
          <div class="modal-body">
            <!-- Важно: .prevent останавливает перезагрузку страницы -->
            <form @submit.prevent="handleSubmit">
              <div v-for="field in fields" :key="field.key" class="mb-3">
                <label class="form-label">{{ field.label }}</label>
                
                <input 
                  v-if="['text', 'number', 'date'].includes(field.type)"
                  :type="field.type" 
                  class="form-control" 
                  v-model="form[field.key]" 
                  :required="field.required"
                  :step="field.step || (field.type === 'number' ? '0.001' : undefined)" 
                  :min="field.min"
                >
                
                <select 
                  v-if="field.type === 'select'"
                  class="form-select" 
                  v-model="form[field.key]"
                  :required="field.required"
                >
                  <option value="" disabled>Выберите...</option>
                  <option v-for="opt in field.options" :key="opt.value" :value="opt.value">
                    {{ opt.text }}
                  </option>
                </select>
              </div>
              <div class="modal-footer">
                <button type="submit" class="btn btn-primary">Сохранить</button>
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
  name: 'GenericForm',
  props: {
    visible: Boolean,
    initialData: Object,
    title: String,
    fields: Array
  },
  data() {
    return { form: {} }
  },
  watch: {
    initialData: {
      handler(val) {
        const newForm = {};

        if (val) {
          for (const key in val) {
            if (Object.prototype.hasOwnProperty.call(val, key)) {
              newForm[key] = val[key];
            }
          }
        }

        this.fields.forEach(f => {
          if (!(f.key in newForm)) {
            newForm[f.key] = f.type === 'number' ? 0 : '';
          }
        });

        this.form = newForm;
        
        console.log("Форма инициализирована:", this.form);
      }
    },
    visible(newVal) {
      if (!newVal) {
        this.form = {}; 
      }
    }
  },
  methods: {
    handleSubmit(e) {
      if (e && e.preventDefault) e.preventDefault();

      const cleanData = {};
      
      this.fields.forEach(f => {
        let value = this.form[f.key];

        if (f.type === 'number') {
          if (value === '' || value === null || value === undefined) {
            value = null;
          } else {
            value = Number(value);
          }
        }
        
        if (f.type === 'select' && value === '') {
          value = null;
        }

        cleanData[f.key] = value;
      });

      console.log("Отправляемые данные:", cleanData);
      this.$emit('submit', cleanData);
    }
  }
}
</script>

<style scoped>
.modal-mask { position: fixed; z-index: 9998; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.5); display: flex; justify-content: center; align-items: center; }
.modal-wrapper { width: 100%; max-width: 500px; padding: 20px; }
.modal-container { background-color: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.33); }
.modal-header { padding: 15px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; }
.modal-body { padding: 20px; }
.modal-footer { padding: 15px; border-top: 1px solid #eee; display: flex; justify-content: flex-end; gap: 10px; }
</style>