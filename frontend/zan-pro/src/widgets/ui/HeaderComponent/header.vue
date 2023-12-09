<script>
    export default {
        data() {
            return {
                isBurgerActive: false,
            };
        },
        methods: {
            toggleBurger() {
                this.isBurgerActive = !this.isBurgerActive;
            },
        },
    };
</script>

<template>
    <header>
        <router-link to="/">
            <div class="logo">
                <img src="../../model/logo.svg" alt="svg logo" />
                <p>Work & Study in Poland</p>
            </div>
        </router-link>
        <nav>
            <ul>
                <router-link to="/"
                    ><li>
                        <p>{{ $t("navHome") }}</p>
                    </li></router-link
                >
                <router-link to="/employment"
                    ><li>
                        <p>{{ $t("navWork") }}</p>
                    </li></router-link
                >
                <router-link to="/contact"
                    ><li>
                        <p>{{ $t("navContact") }}</p>
                    </li></router-link
                >
            </ul>
        </nav>
        <div class="burger-container">
            <label
                class="burger-menu"
                :class="{ active: isBurgerActive }"
                @click="toggleBurger"
            >
                <span class="burger-line"></span>
                <span class="burger-line"></span>
                <span class="burger-line"></span>
            </label>
            <nav class="nav-links" :class="{ active: isBurgerActive }">
                <ul>
                    <router-link to="/"
                        ><li>{{ $t("navHome") }}</li></router-link
                    >
                    <router-link to="/employment"
                        ><li>{{ $t("navWork") }}</li></router-link
                    >
                    <router-link to="/contact"
                        ><li>{{ $t("navContact") }}</li></router-link
                    >
                </ul>
            </nav>
        </div>
    </header>
</template>
