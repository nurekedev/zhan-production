import axios from 'axios';
import { reactive } from 'vue';
import { i18n } from '@/main';

const state = reactive({
    form: {
        name: '',
        phone: '',
    },
    responseMessage: '',
    errorMessage: '',
    resStatus: '',
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
    CLEAR_MESSAGE(state) {
        state.responseMessage = '';
    },
    UPDATE_ERROR(state, payload) {
        state.errorMessage = payload;
    },
    UPDATE_STATUS(state, payload) {
        state.resStatus = payload
    }
};

const actions = {
    async submitForm({ commit }, payload) {
        commit('CLEAR_MESSAGE');
        try {
            const res = await axios.post(`${i18n.global.locale.value}/submit-contact/`, payload);        
            commit('UPDATE_MESSAGE', res.data.message);
        } catch (e) {
            if(e.response.status === '500') {
                commit('UPDATE_STATUS', e.response.status);
            } 
            commit('UPDATE_MESSAGE', 'You filled wrong data!')
            throw e;
        }
    },
    async questionSubmit({ commit }, payload) {
        commit('CLEAR_MESSAGE');
        try {
            const res = await axios.post(`${i18n.global.locale.value}/submit-question/`, payload);
            commit('UPDATE_MESSAGE', res.data.message);
        } catch (e) {
            if(e.response.status === '500') {
                commit('UPDATE_STATUS', e.response.status);
            } 
            commit('UPDATE_MESSAGE', 'You filled wrong data!')
            throw e;
        }
    },
    async submitVacancy({ commit }, payload) {
        commit('CLEAR_MESSAGE');
        try {
            const endPoint = `${i18n.global.locale.value}/api/v1/vacancies/${payload.slug}/submit/`;
            const res = await axios.post(endPoint, payload.form, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                }
            });
            commit('UPDATE_MESSAGE', res.data.message)
        } catch (e) {
            if(e.response.status === '500') {
                commit('UPDATE_STATUS', e.response.status);
            } 
            commit('UPDATE_MESSAGE', 'You filled wrong data!')
            throw e;
        }
    }
};

const getters = {
    getPhone: state => state.form.phone_number,
    getName: state => state.form.full_name, 
    getMessage: state => state.responseMessage,
    errorMessage: state => state.errorMessage,
    responseStatus: state => state.resStatus,
};

const homeForm = {
    state,
    mutations,
    actions,
    getters
}

export default homeForm;