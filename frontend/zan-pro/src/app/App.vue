<script setup>
import {RouterView} from 'vue-router'
import HeaderComponent from '../widgets/ui/HeaderComponent/header.vue';
import FooterComponent from '../widgets/ui/FooterCompomemt/footer.vue'
import LanguageChangerComponent from '../features/ui/LanguageChangerComponent/languageChangerComponent.vue';
</script>

<template>
    <HeaderComponent />
    <RouterView />
    <LanguageChangerComponent />
    <FooterComponent />
</template>
