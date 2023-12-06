import { createStore } from 'vuex';
import homeForm from './modules/form'
import vacancy from './modules/vacancy'
import review from './modules/review'
import locale from './modules/locale'

const store = createStore({
    modules: {
        homeForm,
        vacancy,
        review,
        locale
    }
});

export default store;