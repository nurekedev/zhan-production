<script>
    import { ref } from "vue";
    import { useStore } from "vuex";
    import { computed } from "vue";
    import { i18n } from "../../../main";

    export default {
        name: "LocaleChanger",
        setup() {
            // States
            const store = useStore();
            const showDropdown = ref(false);
            localStorage.setItem("locale", "ru");

            // Computed
            const activeLocale = computed(() => store.getters.activeLocale);

            // Methods
            const changeLocale = (newLocale) => {
                store.dispatch("updateLocale", newLocale);
                localStorage.setItem("locale", newLocale);
                toggleDropdown();
            };
            const toggleDropdown = () => {
                showDropdown.value = !showDropdown.value;
            };
            return {
                showDropdown,
                changeLocale,
                toggleDropdown,
                activeLocale,
            };
        },
    };
</script>

<template>
    <div class="locale-container">
        <div class="active-locale" @click="toggleDropdown">
            <p>{{ activeLocale }}</p>
        </div>
        <div v-if="showDropdown" class="dropdown-content">
            <div class="locale" @click="changeLocale('ru')"><p>ru</p></div>
            <div class="locale" @click="changeLocale('kk')"><p>kk</p></div>
        </div>
    </div>
</template>