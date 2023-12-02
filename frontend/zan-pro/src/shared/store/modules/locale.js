const state = {
    activeLocale: 'en',
}
const actions = {
    updateLocale({ commit }, payload) {
        commit('SET_LOCALE', payload);
    },
}
const mutations = {
    SET_LOCALE(state, payload) {
        state.activeLocale = payload;
    },
}
const getters = {
    activeLocale: state => state.activeLocale,
}

const locale = {
    state,
    actions,
    mutations,
    getters
}

export default locale;