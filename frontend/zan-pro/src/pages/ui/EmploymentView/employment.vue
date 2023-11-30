<script setup>
import Search from '../../../features/ui/SearchComponent/searchComp.vue';
import EmpItem from '../../../widgets/ui/EmpItemComponent/EmpItemComponent.vue';
import Pagination from '../../../features/ui/PaginationComponent/paginationComponent.vue';
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
                    <EmpItem v-for="i in 6" />
                </div>
                <!-- TODO: Implement pagination logic -->
                <Pagination />
            </div>
        </article>
    </main>
</template>