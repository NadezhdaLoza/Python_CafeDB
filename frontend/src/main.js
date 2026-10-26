import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Импортируем Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// Создание экземпляра приложения Vue
const app = createApp(App)

// Подключаем плагины
app.use(router) // Маршрутизатор
app.use(store) // Хранилище состояния

// Монтируем приложение
app.mount('#app')
