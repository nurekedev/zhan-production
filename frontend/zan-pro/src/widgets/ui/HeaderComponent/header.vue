<script>
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
                <!-- <router-link to="/employment"><li>Трудоустройство в Польше</li></router-link> -->
                <!-- <router-link to="/contact"><li>Контакты</li></router-link> -->
                <router-link to="/employment"><li>{{ $t('navWork') }}</li></router-link>
                <router-link to="/contact"><li>{{ $t('navContact') }}</li></router-link>
            </ul>
        </nav>
        <div class="burger-btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="8" viewBox="0 0 32 8" fill="none">
                <rect width="32" height="2" fill="black" />
                <rect y="6" width="32" height="2" fill="black" />
            </svg>
        </div>
    </header>
</template>