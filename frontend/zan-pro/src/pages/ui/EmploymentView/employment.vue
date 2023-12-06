<script>
import Search from '../../../features/ui/SearchComponent/searchComp.vue';
import EmpItem from '../../../widgets/ui/EmpItemComponent/EmpItemComponent.vue';
import Pagination from '../../../features/ui/PaginationComponent/paginationComponent.vue';
import { onMounted, watch } from 'vue';
import { computed, reactive, ref, toRefs } from 'vue';
import { useStore } from 'vuex';
import { useI18n } from 'vue-i18n'
export default {
    name: 'EmploymentPage',
    components: {
        Search,
        EmpItem,
        Pagination,
    },
    setup() {
        // States
        const { t, locale } = useI18n();
        const store = useStore();
        const vacancies = ref([]);
        
        // Computed
        const allVacancies = computed(() => store.getters.allVacancies);
        const oldLocale = computed(() => store.getters.oldLocale);
        const activeLocale = computed(() => store.getters.activeLocale);

        // Methods

        // get all vacancies on component mount
        onMounted(
            () => {
                store.dispatch('fetchVacancies', localStorage.getItem('locale'));
            }
        );
        // checks locale changing and triggers on change
        watch(locale, async (newLocale, oldLocale) => {
            console.log('new:', newLocale);
            console.log('old:', oldLocale);
            if (newLocale !== oldLocale) {
                store.dispatch('fetchVacancies', locale.value);
            }
        });
        
        return {
            vacancies,
            allVacancies,
            t
        }
    }
}
</script>

<template>
    <main class="emp-main">
        <section>
            <img src="../../model/emp.jpeg">
            <div class="page-title">
                <p>{{ $t('navWork') }}</p>
            </div>
        </section>
        <article>
            <div class="wrap">
                <div class="wrap-title">
                    <h1>{{ $t('employmentMainHeader') }}</h1>
                    <!-- TODO: Implement search logic -->
                    <Search />
                </div>
                <div class="wrap-content">
                    <EmpItem 
                        v-for="vacancy in allVacancies"
                        :key="vacancy.slug"
                        :title="vacancy.name"
                        :slug="vacancy.slug"
                        :salary="vacancy.salary"
                        :companyName="vacancy.company.name"
                        :city="vacancy.city.name"
                        :picURL="vacancy.model_pic"/>
                </div>
                <!-- TODO: Implement pagination logic -->
                <Pagination />
            </div>
        </article>
    </main>
</template>