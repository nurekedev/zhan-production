import { createStore } from 'vuex';
import homeForm from './modules/form'

const store = createStore({
    modules: {
        homeForm,
    }
});

export default store;