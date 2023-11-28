<script>
export default {
    data() {
        return {
            showDropdown: false,
        }
    },
    methods: {
        changeLocale(locale) {
            this.$i18n.locale = locale;
            this.showDropdown = !this.showDropdown;
        },
        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        }
    },
}
</script>

<template>
    <div class="locale-container">
        <div class="active-locale" @click="toggleDropdown"><p>{{ this.$i18n.locale }}</p></div>
        <div v-if="showDropdown" class="dropdown-content">
            <div class="locale" @click="changeLocale('en')"><p>en</p></div>
            <div class="locale" @click="changeLocale('pl')"><p>pl</p></div>
            <div class="locale" @click="changeLocale('kz')"><p>kz</p></div>
        </div>
    </div>
</template>