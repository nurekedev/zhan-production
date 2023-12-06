import './app/style/main.scss';
import { createApp } from 'vue';
import { createI18n } from 'vue-i18n';
import store from './shared/store/index.js';
import App from './app/App.vue';
import router from './app/providers/index.js';
import ru from './app/providers/locale/ru.json';
import kk from './app/providers/locale/kk.json';
import en from './app/providers/locale/en.json';
import pl from './app/providers/locale/pl.json';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

const i18n = createI18n({
    legacy: false,
    locale: localStorage.getItem('locale'),
    fallbackLocale: 'en',
    messages: {
        ru: ru,
        en: en,
        kk: kk,
        pl: pl,
    }
})

createApp(App).use(router, axios).use(store).use(i18n).mount('#app');

export { i18n };