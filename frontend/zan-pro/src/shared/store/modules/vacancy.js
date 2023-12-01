import { onBeforeUpdate, reactive } from "vue";
import i18n from '../../../app/providers/locale';
import axios from 'axios';

const state = reactive({
    vacancies: [],
    vacancy: {
        name: '',
        salary: '',
        city: {},
        company: {},
        responsibility_text: '',
        working_condition_text: '',
        accomodation: '',
        additional_text: '',
    },
});
const actions = {
    async fetchVacancies({ commit }) {
        try {
            const res = await axios.get(`${i18n.global.locale}/api/v1/vacancies/`);
            commit('UPDATE_VACANCIES', res.data.results);
            console.log(res.data.results);
        } catch (e) {
            console.log(e);
            throw e;
        }
    },
};
const mutations = {
    UPDATE_VACANCIES(state, payload) {
        state.vacancies = payload;
    }
};
const getters = {
    allVacancies: state => state.vacancies,
};

const vacancy = {
    state,
    actions,
    mutations,
    getters
}

export default vacancy;