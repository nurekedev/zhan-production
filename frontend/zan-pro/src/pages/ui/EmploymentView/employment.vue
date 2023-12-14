<script>
    import Search from "../../../features/ui/SearchComponent/searchComp.vue";
    import EmpItem from "../../../widgets/ui/EmpItemComponent/EmpItemComponent.vue";
    import Pagination from "../../../features/ui/PaginationComponent/paginationComponent.vue";
    import { onMounted, watch } from "vue";
    import { computed, reactive, ref, toRefs, watchEffect } from "vue";
    import { useStore } from "vuex";
    import { useI18n } from "vue-i18n";
    import { onBeforeMount } from "vue";
    import { onUpdated } from "vue";
    import router from "../../../app/providers";
    export default {
        name: "EmploymentPage",
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
            const search = ref("");

            // Computed
            const allVacancies = computed(() => store.getters.allVacancies);
            const vacanciesLength = computed(
                () => store.getters.vacanciesLength
            );
            const responseStatus = computed(() => store.getters.resStatus);
            const isLoading = computed(() => store.getters.isLoading);
            // Methods

            // get all vacancies on component mount
            onBeforeMount(async () => {
                try {
                    await store.dispatch("fetchVacancies", {
                        locale: locale.value,
                        page: 1,
                    });
                } catch (e) {
                    if (responseStatus.value === 500) {
                        router.push("/error500");
                    }
                }
            });
            // checks locale changing and triggers on change
            watch(locale, async (newLocale, oldLocale) => {
                try {
                    if (newLocale !== oldLocale) {
                        await store.dispatch("fetchVacancies", {
                            locale: locale.value,
                            page: 1,
                        });
                    }
                } catch (e) {
                    if (responseStatus.value === 500) {
                        router.push("/error500");
                    }
                }
            });

            watchEffect(async () => {
                try {
                    await store.dispatch("searchVacancies", {
                        search: search.value,
                        locale: locale.value,
                        page: 1,
                        page_size: 6,
                    });
                } catch (e) {
                    if (responseStatus.value === 500) {
                        router.push("/error500");
                    }
                }
            });

            return {
                vacancies,
                allVacancies,
                t,
                search,
                vacanciesLength,
                isLoading,
            };
        },
    };
</script>

<template>
    <main class="emp-main">
        <section>
            <img src="../../model/emp.jpeg" />
            <div class="page-title">
                <p>{{ $t("navWork") }}</p>
            </div>
        </section>
        <article>
            <div class="wrap">
                <div class="wrap-title">
                    <h1>{{ $t("employmentMainHeader") }}</h1>
                    <!-- TODO: Implement search logic -->
                    <div class="input-container">
                        <input type="search" placeholder="" v-model="search" />
                        <label>{{ $t("formSearch") }}</label>
                        <img src="../../model/search.svg" />
                    </div>
                </div>
                <div class="wrap-content">
                    <div class="vacancy-items" v-if="!isLoading">
                        <EmpItem
                            v-for="vacancy in allVacancies"
                            :key="vacancy.slug"
                            :title="vacancy.name"
                            :slug="vacancy.slug"
                            :salary="vacancy.salary"
                            :companyName="vacancy.company.name"
                            :city="vacancy.city.name"
                            :picURL="vacancy.model_pic"
                        />
                    </div>
                    <div class="vacancy-skeleton" v-else>
                        <img src="../../model/refresh.svg" alt="" />
                    </div>
                </div>
                <!-- TODO: Implement pagination logic -->
                <Pagination :pages="vacanciesLength" />
            </div>
        </article>
    </main>
</template>
