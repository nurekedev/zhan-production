<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import { i18n } from '../../../main';
import { computed } from 'vue';

export default {
    name: 'LocaleChanger',
    setup() {
        // States
        const store = useStore();
        const showDropdown = ref(false);

        // Computed
        const activeLocale = computed(() => store.getters.activeLocale);
        // Methods
        const changeLocale = (locale) => {
            store.dispatch('updateLocale', locale);
            localStorage.setItem('locale', locale);
            i18n.global.locale = locale;
            toggleDropdown();
        };
        const toggleDropdown = () => {
            showDropdown.value = !showDropdown.value;
        };
        return {
            showDropdown,
            changeLocale,
            toggleDropdown,
        }
    },
}
</script>

<template>
    <div class="locale-container">
        <div class="active-locale" @click="toggleDropdown"><p>{{ this.$i18n.locale }}</p></div>
        <div v-if="showDropdown" class="dropdown-content">
            <div class="locale" @click="changeLocale('ru')"><p>ru</p></div>
            <div class="locale" @click="changeLocale('pl')"><p>pl</p></div>
            <div class="locale" @click="changeLocale('kk')"><p>kk</p></div>
            <div class="locale" @click="changeLocale('en')"><p>en</p></div>
        </div>
    </div>
</template>