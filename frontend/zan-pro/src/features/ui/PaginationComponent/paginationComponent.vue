<script>
    import { computed } from "vue";
    import { ref } from "vue";
    import { useI18n } from "vue-i18n";
    import { useStore } from "vuex";

    export default {
        name: "Pagination",
        props: { pages: "" },
        setup(props) {
            const { locale } = useI18n();
            const store = useStore();
            const currentPage = ref(1);
            const showButtonPrev = ref(false);
            const showButtonNext = ref(true);

            let numberOfPages = computed(() => store.getters.numberOfPages);
            // Methods
            const loadPage = async (page) => {
                await store.dispatch("fetchVacancies", {
                    locale: locale.value,
                    page: page,
                });
            };
            const loadNextPage = async () => {
                if (currentPage.value < Math.ceil(numberOfPages.value)) {
                    currentPage.value++;
                } else {
                    currentPage.value = Math.ceil(numberOfPages.value);
                }
                await store.dispatch("fetchVacancies", {
                    locale: locale.value,
                    page: currentPage.value,
                });
            };
            const loadPrevPage = async () => {
                if (currentPage.value > 1) {
                    currentPage.value--;
                } else {
                    currentPage.value = 1;
                }
                await store.dispatch("fetchVacancies", {
                    locale: locale.value,
                    page: currentPage.value,
                });
            };
            const loadLastPage = async (page) => {
                await store.dispatch("fetchVacancies", {
                    locale: locale.value,
                    page: page,
                });
            };

            return {
                loadPage,
                loadNextPage,
                loadPrevPage,
                loadLastPage,
                numberOfPages,
                showButtonPrev,
                showButtonNext,
                currentPage,
            };
        },
    };
</script>
<template>
    <div class="pagination">
        <img src="../../model/left-arrow.svg" @click="loadPrevPage" />
        <div class="p-item">
            <span @click="loadPage(1)"> 1 </span>
            <span class="active">
                {{ currentPage }}
            </span>
            <span
                v-if="numberOfPages > 2"
                @click="loadLastPage(Math.ceil(numberOfPages))"
                class="lastPage"
            >
                {{ Math.ceil(numberOfPages) }}
            </span>
        </div>
        <img src="../../model/right-arrow.svg" @click="loadNextPage" />
    </div>
</template>
