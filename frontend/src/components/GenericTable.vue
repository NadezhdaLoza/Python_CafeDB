<template>
  <table class="table table-striped table-bordered">
    <thead>
      <tr>
        <th v-for="col in columns" :key="col.key">{{ col.label }}</th>
        <th style="width: 150px;">Действия</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in items" :key="item[idField]">
        <td v-for="col in columns" :key="col.key">
          {{ item[col.key] }}
        </td>
        <td>
          <button class="btn btn-sm btn-warning me-2" @click="$emit('edit', item)">&#9998;</button>
          <button class="btn btn-sm btn-danger" @click="$emit('delete', item[idField])">&#128465;</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'GenericTable',
  props: {
    items: { type: Array, required: true },
    columns: { type: Array, required: true },
    idField: { type: String, default: 'id' }
  }
}
</script>

<style scoped>
.btn-sm { padding: 0.25rem 0.5rem; font-size: 0.875rem; }
</style>