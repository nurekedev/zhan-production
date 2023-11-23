<script setup>
import {RouterView} from 'vue-router'
import HeaderComponent from '../widgets/ui/HeaderComponent/header.vue';
import FooterComponent from '../widgets/ui/FooterCompomemt/footer.vue'
</script>

<template>
    <HeaderComponent />
    <RouterView />
    <FooterComponent />
</template>
