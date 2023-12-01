import { createStore } from 'vuex';
import homeForm from './modules/form'
import vacancy from './modules/vacancy'

const store = createStore({
    modules: {
        homeForm,
        vacancy,
    }
});

export default store;