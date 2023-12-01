import { createI18n } from 'vue-i18n';
import ru from './locale/ru.json';
import en from './locale/en.json';
import kk from './locale/kk.json';
import pl from './locale/pl.json';



const i18n = createI18n({
    locale: 'en',
    fallbackLocale: 'en',
    messages: {
        ru: ru,
        en: en,
        kk: kk,
        pl: pl,
    }
})

export default i18n;