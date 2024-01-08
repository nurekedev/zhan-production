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
        let locale = payload;
        if (locale === 'pl') {
            locale = 'en';
        }
        try {
            const res = await axios.get(`${locale}/api/v1/reviews/`);
            commit('UPDATE_REVIEWS', res.data)
        } catch (e) {
            if(e.response.status === '500') {
                commit('UPDATE_STATUS', e.response.status);
            }
            throw e;
        }

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