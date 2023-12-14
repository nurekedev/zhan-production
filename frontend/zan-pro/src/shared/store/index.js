import { createStore } from 'vuex';
import homeForm from './modules/form';
import vacancy from './modules/vacancy';
import locale from './modules/locale';
import social from './modules/social';

const store = createStore({
    modules: {
        homeForm,
        vacancy,
        locale,
        social,
    },
});

export default store;
