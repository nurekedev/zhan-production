import { reactive } from "vue";
import axios from 'axios';
import { i18n } from '@/main';

const state = reactive({
    vacancies: [],
    vacancy: {
        name: '',
        salary: '',
        slug: '',
        city: {},
        company: {},
        responsibility_text: '',
        working_condition_text: '',
        accomodation: '',
        additional_text: '',
    },
    similar_vacancies: [],
});
const actions = {
    async fetchVacancies({ commit }, payload) {
        try {
            console.log(payload);
            const res = await axios.get(`${payload}/api/v1/vacancies/`);
            commit('UPDATE_VACANCIES', res.data.results);
            console.log(res.data.results);
        } catch (e) {
            console.log(e);
            throw e;
        }
    },
    async fetchVacancy({ commit }, slug) {
        try {
            const res = await axios.get(`${i18n.global.locale.value}/api/v1/vacancies/${slug}`);
            console.log(i18n.global.locale);
            commit('UPDATE_SIMILAR', res.data.similar_vacancies);
            commit('UPDATE_VACANCY', res.data.vacancy_details);
        } catch (e) {
            console.log(e);
            throw e;
        }
    }
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
    }
};
const getters = {
    allVacancies: state => state.vacancies,
    currentVacancy: state => state.vacancy,
    allSimilarVacancies: state => state.similar_vacancies
};

const vacancy = {
    state,
    actions,
    mutations,
    getters
}

export default vacancy;