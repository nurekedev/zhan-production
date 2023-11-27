import { createI18n } from 'vue-i18n';
import ru from './locale/ru.json';
import en from './locale/en.json';
import kz from './locale/kz.json';
import pl from './locale/pl.json';

function loadLocaleMessages() {
    const locales = [{ru: ru, en: en, kz: kz, pl: pl}];
    const messages = {};
    locales.forEach(lang => {
        const key = Object.keys(lang);
        messages[key] = lang[key];
    });
    return messages;
}

const i18n = createI18n({
    locale: 'kz',
    fallbackLocale: 'ru',
    messages: {
        ru: ru,
        en: en,
        kz: kz,
        pl: pl,
    }
})

export default i18n;