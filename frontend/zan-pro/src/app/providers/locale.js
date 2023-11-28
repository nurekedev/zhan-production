import { createI18n } from 'vue-i18n';
import ru from './locale/ru.json';
import en from './locale/en.json';
import kz from './locale/kz.json';
import pl from './locale/pl.json';



const i18n = createI18n({
    locale: 'en',
    fallbackLocale: 'en',
    messages: {
        ru: ru,
        en: en,
        kz: kz,
        pl: pl,
    }
})

export default i18n;