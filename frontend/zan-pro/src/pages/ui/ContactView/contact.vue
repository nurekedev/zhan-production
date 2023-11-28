<script setup>
import LanguageChangerComponent from '../../../features/ui/LanguageChangerComponent/languageChangerComponent.vue';
</script>

<template>
    <main class="contact">
        <section>
            <div>{{ $t('navContact') }}</div>
        </section>
        <article class="main-article">
            <div class="main-text">
                <p>{{ $t('contactsMainText') }}</p>
            </div>
            <div class="form-group">
                <form action="" method="post">
                    <p>{{ $t('contactsFormHeader') }}</p>
                    <div class="input-container">
                        <input type="text" name="name" id="name" placeholder="">
                        <label for="name">{{ $t('formLabelName') }}</label>
                    </div>
                    <div class="input-container">
                        <input type="text" name="number" id="number" placeholder="">
                        <label for="number">{{ $t('formLabelNumber') }}</label>
                    </div>
                    <div class="input-container">
                        <input type="email" name="email" id="email" placeholder="">
                        <label for="email">{{ $t('formLabelMail') }}</label>
                    </div>
                    <div class="input-container">
                        <textarea name="additional" id="additional" cols="30" rows="10" placeholder=""></textarea>
                        <label for="additional">{{ $t('formLabelOptional') }}</label>
                    </div>
                    <button type="submit">{{ $t('formButton') }}</button>
                </form>
            </div>
        </article>
        <LanguageChangerComponent />
    </main>
</template>