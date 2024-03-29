import { reactive } from 'vue';
import axios from 'axios';
import { i18n } from '@/main';

const state = reactive({
    vacancies: [],
    numberOfPages: 0,
    isLoading: null,
    resStatus: '',
    currentPage: 1,
    vacancy: {
        name: '',
        salary: '',
        slug: '',
        city: {},
        company: {},
        responsibility_text: '',
        requirement_text: '',
        schedule: '',
        working_condition_text: '',
        accomodation: '',
        nutrition: '',
        additional_text: '',
    },
    similar_vacancies: [],
});
const actions = {
    async fetchVacancies({ commit }, payload) {
        commit('SET_IS_LOADING', true);
        let { locale, page } = payload;
        commit('SET_PAGE', page);
        try {
            const res = await axios.get(
                `${locale}/api/v1/vacancies/?page=${state.currentPage}&page_size=6`
            );
            commit('UPDATE_VACANCIES', res.data.results);
            commit('UPDATE_NUMBER_OF_PAGES', res.data.count / 6);
        } catch (e) {
            if (e.response.status === 500) {
                commit('UPDATE_STATUS', e.response.status);
            }
            throw e;
        }
        commit('SET_IS_LOADING', false);
    },
    async searchVacancies({ commit }, payload) {
        commit('SET_IS_LOADING', true);
        let { locale, page, page_size, search } = payload;

        try {
            const res = await axios.get(
                `${locale}/api/v1/vacancies/?page=${page}&page_size=${page_size}&search=${search}`
            );
            commit('UPDATE_VACANCIES', res.data.results);
        } catch (e) {
            if (e.response.status === 500) {
                commit('UPDATE_STATUS', e.response.status);
            }
            throw e;
        }
        commit('SET_IS_LOADING', false);
    },
    async fetchVacancy({ commit }, payload) {
        let locale = payload.locale;

        try {
            const res = await axios.get(
                `${locale}/api/v1/vacancies/${payload.slug}`
            );
            commit('UPDATE_SIMILAR', res.data.similar_vacancies);
            commit('UPDATE_VACANCY', res.data.vacancy_details);
        } catch (e) {
            if (e.response.status === 500) {
                commit('UPDATE_STATUS', e.response.status);
            }
            throw e;
        }
    },
    updateActivePage({ commit }, payload) {
        commit('SET_PAGE', payload);
    },
};
const mutations = {
    UPDATE_VACANCIES(state, payload) {
        state.vacancies = payload;
    },
    UPDATE_VACANCY(state, payload) {
        state.vacancy = payload;
    },
    UPDATE_SIMILAR(state, payload) {
        state.similar_vacancies = payload;
    },
    UPDATE_NUMBER_OF_PAGES(state, payload) {
        state.numberOfPages = payload;
    },
    SET_IS_LOADING(state, payload) {
        state.isLoading = payload;
    },
    UPDATE_STATUS(state, payload) {
        state.resStatus = payload;
    },
    SET_PAGE(state, payload) {
        state.currentPage = payload;
    },
};
const getters = {
    allVacancies: (state) => state.vacancies,
    currentVacancy: (state) => state.vacancy,
    allSimilarVacancies: (state) => state.similar_vacancies,
    numberOfPages: (state) => state.numberOfPages,
    isLoading: (state) => state.isLoading,
    resStatus: (state) => state.resStatus,
    activePage: (state) => state.currentPage,
};

const vacancy = {
    state,
    actions,
    mutations,
    getters,
};

export default vacancy;
