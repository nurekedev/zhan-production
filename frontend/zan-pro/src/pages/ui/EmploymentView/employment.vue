<script>
import Search from '../../../features/ui/SearchComponent/searchComp.vue';
import EmpItem from '../../../widgets/ui/EmpItemComponent/EmpItemComponent.vue';
import Pagination from '../../../features/ui/PaginationComponent/paginationComponent.vue';
import { onMounted } from 'vue';
import { computed, reactive, ref, toRefs } from 'vue';
import { useStore } from 'vuex';
export default {
    name: 'EmploymentPage',
    components: {
        Search,
        EmpItem,
        Pagination,
    },
    setup() {
        // States
        const store = useStore();
        const vacancies = ref([]);
        
        // Computed
        const allVacancies = computed(() => store.getters.allVacancies);

        // Methods

        // get all vacancies on component mount
        onMounted(
            // FIXME: update data when locale changes
            () => {
                store.dispatch('fetchVacancies');
            }
        );
        
        return {
            vacancies,
            allVacancies,
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
                    <!-- TODO: Implement api request for vacancies -->
                    <EmpItem 
                        v-for="vacancy in allVacancies"
                        :key="vacancy.slug"
                        :title="vacancy.name"
                        :salary="vacancy.salary"
                        :companyName="vacancy.company.name"
                        :city="vacancy.city.name"/>
                </div>
                <!-- TODO: Implement pagination logic -->
                <Pagination />
            </div>
        </article>
    </main>
</template>