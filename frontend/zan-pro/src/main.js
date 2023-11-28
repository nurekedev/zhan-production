import './app/style/main.scss'
import { createApp } from 'vue'
import App from './app/App.vue'
import router from './app/providers'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

createApp(App).use(router, axios).mount('#app')