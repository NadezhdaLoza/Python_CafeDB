<template>
  <div class="home-container">
    <header class="hero-section">
      <h1>Кафе-Пекарня</h1>
      <p class="subtitle">Система управления заказами и персоналом</p>
    </header>

    <div class="dashboard-grid">
      
      <!-- Секция 1: Операции -->
      <section class="panel">
        <div class="panel-header">
          <h2>Операции</h2>
        </div>
        <div class="cards-grid">
          <router-link to="/orders" class="action-card primary">
            <div class="card-info">
              <h3>Заказы (Товарные чеки)</h3>
              <p>Оформление и история продаж</p>
            </div>
          </router-link>
        </div>
      </section>

      <!-- Секция 2: Меню и Кухня -->
      <section class="panel">
        <div class="panel-header">
          <h2>Меню и Кухня</h2>
        </div>
        <div class="cards-grid">
          <router-link to="/dishes" class="action-card">
            <div class="card-info">
              <h3>Блюда</h3>
              <p>Карточка меню и цены</p>
            </div>
          </router-link>
          <router-link to="/categories" class="action-card">
            <div class="card-info">
              <h3>Категории</h3>
              <p>Группы блюд и напитков</p>
            </div>
          </router-link>
          <router-link to="/ingredients" class="action-card">
            <div class="card-info">
              <h3>Ингредиенты</h3>
              <p>Сырье и продукты</p>
            </div>
          </router-link>
          <router-link to="/recipes" class="action-card">
            <div class="card-info">
              <h3>Рецепты</h3>
              <p>Технологические карты</p>
            </div>
          </router-link>
          <router-link to="/suppliers" class="action-card">
            <div class="card-info">
              <h3>Поставщики</h3>
              <p>Контрагенты и закупки</p>
            </div>
          </router-link>
        </div>
      </section>

      <!-- Секция 3: Персонал и Клиенты -->
      <section class="panel">
        <div class="panel-header">
          <h2>Люди</h2>
        </div>
        <div class="cards-grid">
          <router-link to="/employees" class="action-card">
            <div class="card-info">
              <h3>Сотрудники</h3>
              <p>Штат и должности</p>
            </div>
          </router-link>
          <router-link to="/positions" class="action-card small">
            <div class="card-info">
              <h3>Должности</h3>
              <p>Справочник ролей</p>
            </div>
          </router-link>
          <router-link to="/clients" class="action-card">
            <div class="card-info">
              <h3>Клиенты</h3>
              <p>База гостей</p>
            </div>
          </router-link>
          <router-link to="/bonus-cards" class="action-card small">
            <div class="card-info">
              <h3>Бонусные карты</h3>
              <p>Программа лояльности</p>
            </div>
          </router-link>
        </div>
      </section>

    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

/* Hero Section */
.hero-section {
  text-align: center;
  margin-bottom: 50px;
  padding: 40px;
  background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
  border-radius: 16px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.hero-section h1 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 10px;
  font-weight: 700;
}

.subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  margin: 0;
}

/* Dashboard Layout */
.dashboard-grid {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.panel {
  background: #fff;
}

.panel-header {
  margin-bottom: 20px;
  border-left: 5px solid #e67e22; /* Оранжевый акцент */
  padding-left: 15px;
}

.panel-header h2 {
  margin: 0;
  font-size: 1.5rem;
  color: #2c3e50;
}

/* Cards Grid */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}

/* Card Styles */
.action-card {
  display: flex;
  align-items: center;
  background: #fff;
  border: 1px solid #eaeaea;
  border-radius: 12px;
  padding: 20px;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.action-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.08);
  border-color: #e67e22;
}

.action-card.primary {
  background: #fff8f0;
  border: 1px solid #ffe0b2;
}

.action-card.primary:hover {
  background: #fff;
}

.card-info {
  width: 100%;
  text-align: left;
}

.card-info h3 {
  margin: 0 0 5px 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #2c3e50;
}

.card-info p {
  margin: 0;
  font-size: 0.9rem;
  color: #7f8c8d;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .hero-section h1 {
    font-size: 2rem;
  }
  
  .cards-grid {
    grid-template-columns: 1fr;
  }
  
  .action-card {
    padding: 15px;
  }
}
</style>