import axios from 'axios';
import { reactive } from 'vue';
import i18n from '../../../app/providers/locale';

const state = reactive({
    form: {
        name: '',
        phone: '',
    },
    responseMessage: '',
});

const mutations = {
    UPDATE_FORM(state, payload) {
        state.form = payload;
    },
    UPDATE_FULLNAME(state, payload) {
        state.form.name = payload;
    },
    UPDATE_PHONE(state, payload) {
        state.form.phone = payload;
    },
    UPDATE_MESSAGE(state, payload) {
        state.responseMessage = payload;
    },
};

const actions = {
    async submitForm({ commit }, payload) {
        try {
            const res = await axios.post(`${i18n.global.locale}/submit-contact/`, payload);          
            commit('UPDATE_MESSAGE', res.data.message);
        } catch (error) {
            console.log(error);
            throw error;
        }
    },
    async questionSubmit({ commit }, payload) {
      try {
            const res = await axios.post(`${i18n.global.locale}/submit-question/`, payload);
            commit('UPDATE_MESSAGE', res.data.message);
      } catch (e) {
            console.log(e);
            throw e;
      }
    },
};

const getters = {
    getPhone: state => state.form.phone_number,
    getName: state => state.form.full_name, 
    getMessage: state => state.responseMessage,
};

const homeForm = {
    state,
    mutations,
    actions,
    getters
}

export default homeForm;