<template>
  <div id="app">
    <!-- Навигационное меню -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top shadow-sm">
      <div class="container-fluid">
        <!-- Логотип/название приложения -->
        <router-link class="navbar-brand d-flex align-items-center" to="/">
          Кафе-пекарня
        </router-link>
        
        <!-- Кнопка для мобильного меню -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <!-- Основное меню -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/" exact-active-class="active">Главная</router-link>
            </li>
            
            <!-- Разделитель -->
            <li class="nav-item"><div class="vr bg-secondary mx-2 my-auto d-none d-lg-block"></div></li>

            <!-- Группа: Операции -->
            <li class="nav-item">
              <router-link class="nav-link" to="/orders">Заказы (Товарные чеки)</router-link>
            </li>

            <!-- Группа: Меню -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="menuDropdown" role="button" data-bs-toggle="dropdown">
                Меню
              </a>
              <ul class="dropdown-menu">
                <li><router-link class="dropdown-item" to="/dishes">Блюда</router-link></li>
                <li><router-link class="dropdown-item" to="/categories">Категории</router-link></li>
                <li><hr class="dropdown-divider"></li>
                <li><router-link class="dropdown-item" to="/ingredients">Ингредиенты</router-link></li>
                <li><router-link class="dropdown-item" to="/recipes">Рецепты</router-link></li>
                <li><router-link class="dropdown-item" to="/suppliers">Поставщики</router-link></li>
              </ul>
            </li>

            <!-- Группа: Люди -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="peopleDropdown" role="button" data-bs-toggle="dropdown">
                Люди
              </a>
              <ul class="dropdown-menu">
                <li><router-link class="dropdown-item" to="/employees">Сотрудники</router-link></li>
                <li><router-link class="dropdown-item" to="/positions">Должности</router-link></li>
                <li><hr class="dropdown-divider"></li>
                <li><router-link class="dropdown-item" to="/clients">Клиенты</router-link></li>
                <li><router-link class="dropdown-item" to="/bonus-cards">Бонусные карты</router-link></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Основное содержимое -->
    <div class="container-fluid mt-4 px-4">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #333;
  background-color: #f8f9fa;
  min-height: 100vh;
}

/* Стили для навбара */
.navbar {
  background-color: #2c3e50 !important; /* Темно-синий/серый цвет */
}

.navbar-brand {
  font-weight: 700;
  font-size: 1.25rem;
  color: #fff !important;
}

.nav-link {
  font-weight: 500;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #e67e22 !important; /* Оранжевый акцент при наведении */
}

.nav-link.active {
  color: #e67e22 !important;
  font-weight: 600;
}

/* Адаптивность для мобильных */
@media (max-width: 991px) {
  .vr {
    display: none !important;
  }
}
</style>