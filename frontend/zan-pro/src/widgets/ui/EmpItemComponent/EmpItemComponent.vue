<script>
    export default {
        name: 'EmpItem',
        props: {
            title: '',
            slug: '',
            salary: '',
            companyName: '',
            city: '',
            picURL: '',
        },
    };
</script>

<template>
    <div class="item">
        <img :src="picURL" alt="vacancy picture" />
        <article>
            <div class="text">
                <h1>{{ title }}</h1>
                <h2>{{ salary }}</h2>
                <h3>{{ companyName }}</h3>
                <h3>{{ city }}</h3>
            </div>
            <div class="btn">
                <button>
                    <router-link :to="'/employment/' + slug + '/'">{{
                        $t('cardButtonRespond')
                    }}</router-link>
                </button>
            </div>
        </article>
    </div>
</template>
