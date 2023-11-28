import './app/style/main.scss'

import { createApp } from 'vue'
import App from './app/App.vue'
import router from './app/providers/index.js'
import i18n from './app/providers/locale.js';
import axios from 'axios'
import store from './shared/store/';

axios.defaults.baseURL = 'http://127.0.0.1:8000/'


createApp(App).use(router, axios).use(store).use(i18n).mount('#app')