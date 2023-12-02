import { reactive } from "vue";
import axios from 'axios';
import { i18n } from '@/main';

const state = reactive({
    reviews: [],
    review: {
        author: '',
        text: ''
    }
});
const actions = {
    async fetchReviews({ commit }, payload) {
        const res = await axios.get(`${payload}/api/v1/reviews/`);
        commit('UPDATE_REVIEWS', res.data)

    }
};
const mutations = {
    UPDATE_REVIEW(state, payload) {
        state.review = payload;
    },
    UPDATE_REVIEWS(state, payload) {
        state.reviews = payload;
    },
};
const getters = {
    allReviews: state => state.reviews,
    review: state => state.review,
};

const review = {
    state,
    actions,
    mutations,
    getters,
}

export default review;