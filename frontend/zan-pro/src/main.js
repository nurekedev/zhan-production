import './app/style/main.scss'

import { createApp } from 'vue'
import App from './app/App.vue'
import router from './app/providers'
// import axios from 'axios'

createApp(App).use(router).mount('#app')