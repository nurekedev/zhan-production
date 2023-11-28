<template>
    <div class="item">
        <img src="../../model/Vacancy img.png">
        <article>
            <h1>UX/UI designer</h1>
            <h2>1000$</h2>
            <h3>Частная компания “Company Name”</h3>
            <h3>Варшава</h3>
            <div class="btn">
                <button><router-link to="/employmentDetails">{{ $t('cardButtonRespond') }}</router-link></button>
                <button><router-link to="/contact">{{ $t('cardButtonContact') }}</router-link></button>
            </div>
        </article>
    </div>
</template>

<script setup>

</script>