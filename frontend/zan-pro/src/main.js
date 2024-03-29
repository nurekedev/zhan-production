import "./app/style/main.scss";
import { createApp } from "vue";
import { createI18n } from "vue-i18n";
import store from "./shared/store/index.js";
import App from "./app/App.vue";
import router from "./app/providers/index.js";
import ru from "./app/providers/locale/ru.json";
import kk from "./app/providers/locale/kk.json";
import axios from "axios";

axios.defaults.baseURL =  process.env.API_URL


const i18n = createI18n({
    legacy: false,
    locale: localStorage.getItem("locale"),
    fallbackLocale: "ru",
    messages: {
        ru: ru,
        kk: kk,
    },
});

createApp(App).use(router, axios).use(store).use(i18n).mount("#app");

export { i18n };
