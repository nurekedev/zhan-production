import { i18n } from '@/main';

const state = {
    activeLocale: 'ru',
    oldLocale: '',
}
const actions = {
    updateLocale({ commit }, payload) {
        commit('SET_OLD_LOCALE', i18n.global.locale);
        commit('SET_LOCALE', payload);
        i18n.global.locale.value = payload;
    },
}
const mutations = {
    SET_LOCALE(state, payload) {
        state.activeLocale = payload;
    },
    SET_OLD_LOCALE(state, payload) {
        state.oldLocale = payload;
    }
}
const getters = {
    activeLocale: state => state.activeLocale,
    oldLocale: state => state.oldLocale,
}

const locale = {
    state,
    actions,
    mutations,
    getters
}

export default locale;