const state = {
    form: {
        full_name: '',
        phone_number: '',
      },
    errors: [],
    catch: '',
};

const mutations = {
    updateForm(state, payload) {
        state.form = { ...state.form, ...payload };
      },
    clearErrors(state) {
        state.errors = [];
    },
    addError(state, error) {
        state.errors.push(error);
    },
};

const actions = {
    submitLightForm({ state, commit, formData}) {
        commit('clearErrors');
        commit('updateForm', formData);
  
        if (state.form.full_name === '') {
          commit('addError', 'The name must be filled out');
        }
  
        if (state.form.phone_number === '') {
          commit('addError', 'The content must be filled out');
        }
  
        if (!state.errors.length) {
          axios
            .post(`en/submit-contact/`, state.form)
            .then(response => {
              commit('updateForm', { full_name: '', phone_number: '' });
              // Можно добавить commit('clearErrors'); здесь, если требуется очистка ошибок после успешной отправки
              // this.$emit('submitLightForm', response.data);
            })
            .catch(error => {
              console.error('Error submitting form:', error);
            });
        }
    },
};

const getters = {};

const lightForm = {
state,
mutations,
actions,
getters
}

export default lightForm; 