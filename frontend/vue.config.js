module.exports = {
  // Настройки dev-сервера
  devServer: {
    historyApiFallback: true,  // Поддержка HTML5 History Mode
    hot: true,                 // Горячая перезагрузка модулей
    port: 8090,                // Порт dev-сервера
    host: 'localhost',         // Хост dev-сервера
    allowedHosts: 'all'        // Разрешенные хосты
  },

  // Базовый URL для production сборки
  publicPath: '/',

  // Отключение линтинга при сохранении
  lintOnSave: false,

  // Конфигурация webpack
  configureWebpack: {
    // Включение source maps для отладки
    devtool: 'source-map'
  },

  // Настройки production сборки
  productionSourceMap: false,  // Отключение source maps в production

  // Конфигурация CSS
  css: {
    // Извлечение CSS в отдельные файлы в production
    extract: process.env.NODE_ENV === 'production',
    // Включение source maps для CSS
    sourceMap: true
  }
}

