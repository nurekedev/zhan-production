import axios from 'axios';
import { reactive } from 'vue';

const state = reactive({
    facebookUrl: '',
    vkUrl: '',
    igUrl: '',
    xUrl: '',
});
const actions = {
    async getFbUrl({ commit }) {
        const res = await axios.get('/social-media/facebook');
        commit('SET_FB', res.data.url);
    },
    async getVkUrl({ commit }) {
        const res = await axios.get('/social-media/facebook');
        commit('SET_VK', res.data.url);
    },
    async getIgUrl({ commit }) {
        const res = await axios.get('/social-media/facebook');
        commit('SET_IG', res.data.url);
    },
    async getXUrl({ commit }) {
        const res = await axios.get('/social-media/facebook');
        commit('SET_X', res.data.url);
    },
};
const mutations = {
    SET_FB(state, payload) {
        state.facebookUrl = payload;
    },
    SET_VK(state, payload) {
        state.vkUrl = payload;
    },
    SET_IG(state, payload) {
        state.igUrl = payload;
    },
    SET_X(state, payload) {
        state.xUrl = payload;
    },
};
const getters = {
    getFb: (state) => state.facebookUrl,
    getVk: (state) => state.vkUrl,
    getIg: (state) => state.igUrl,
    getX: (state) => state.xUrl,
};

const social = {
    state,
    actions,
    mutations,
    getters,
};

export default social;
