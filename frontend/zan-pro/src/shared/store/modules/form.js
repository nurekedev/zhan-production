import axios from "axios";
import { reactive } from "vue";
import { i18n } from "@/main";

const state = reactive({
    form: {
        name: "",
        phone: "",
    },
    responseMessage: "",
    errorMessage: "",
    resStatus: "",
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
        state.responseMessage = "";
    },
    UPDATE_ERROR(state, payload) {
        state.errorMessage = payload;
    },
    UPDATE_STATUS(state, payload) {
        state.resStatus = payload;
    },
};

const actions = {
    async submitForm({ commit }, payload) {
        commit("CLEAR_MESSAGE");
        let locale = i18n.global.locale.value;
        try {
            const res = await axios.post(`${locale}/submit-contact/`, payload);
       
            
            if (res.status === 200) {
                commit("UPDATE_STATUS", res.status);
            }
        } catch (e) {
            if (e.response.status === 500) {
                commit("UPDATE_STATUS", e.response.status);
            }
            if (e.response.status === 429) {
                commit("UPDATE_STATUS", e.response.status);
            }
            throw e;
        }
    },

    async questionSubmit({ commit }, payload) {
        commit("CLEAR_MESSAGE");
        let locale = i18n.global.locale.value;

        try {
            const res = await axios.post(`${locale}/submit-question/`, payload);

            commit("UPDATE_MESSAGE", res.data.message);
        } catch (e) {
            if (e.response.status === 200) {
                commit("UPDATE_STATUS", e.response.status);
            }
            if (e.response.status === 500) {
                commit("UPDATE_STATUS", e.response.status);
            }
            if (e.response.status === 429) {
                commit("UPDATE_STATUS", e.response.status);
            }
            throw e;
        }
    },
    async submitVacancy({ commit }, payload) {
        commit("CLEAR_MESSAGE");
        let locale = i18n.global.locale.value;

        try {
            const endPoint = `${locale}/api/v1/vacancies/${payload.slug}/submit/`;
            const res = await axios.post(endPoint, payload.form, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
            // commit("UPDATE_MESSAGE", res.data.message);
        } catch (e) {
            if (e.response.status === 200) {
                commit("UPDATE_STATUS", e.response.status);
            }
            if (e.response.status === 500) {
                commit("UPDATE_STATUS", e.response.status);
            }
            if (e.response.status === 429) {
                commit("UPDATE_STATUS", e.response.status);
            }
            throw e;
        }
    },
    setMessage({ commit }, payload) {
        commit("UPDATE_MESSAGE", payload);
    },
};

const getters = {
    getPhone: (state) => state.form.phone_number,
    getName: (state) => state.form.full_name,
    getMessage: (state) => state.responseMessage,
    errorMessage: (state) => state.errorMessage,
    responseStatus: (state) => state.resStatus,
};

const homeForm = {
    state,
    mutations,
    actions,
    getters,
};

export default homeForm;
