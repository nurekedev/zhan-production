import axios from 'axios';
import { reactive } from 'vue';

const state = reactive({
    facebookUrl: '',
    vkUrl: '',
    igUrl: '',
    xUrl: '',
    waUrl: '',
});
const actions = {
    async getFbUrl({ commit }) {
        const res = await axios.get('/social-media/facebook');
        commit('SET_FB', res.data.url);
    },
    async getVkUrl({ commit }) {
        const res = await axios.get('/social-media/vk');
        commit('SET_VK', res.data.url);
    },
    async getIgUrl({ commit }) {
        const res = await axios.get('/social-media/instagram');
        commit('SET_IG', res.data.url);
    },
    async getXUrl({ commit }) {
        const res = await axios.get('/social-media/twitter');
        commit('SET_X', res.data.url);
    },
    async getWaUrl({ commit }) {
        const res = await axios.get('/social-media/whatsapp');
        commit('SET_WA', res.data.url);
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
    SET_WA(state, payload) {
        state.waUrl = payload;
    },
};
const getters = {
    getFb: (state) => state.facebookUrl,
    getVk: (state) => state.vkUrl,
    getIg: (state) => state.igUrl,
    getX: (state) => state.xUrl,
    getWa: (state) => state.waUrl,
};

const social = {
    state,
    actions,
    mutations,
    getters,
};

export default social;
