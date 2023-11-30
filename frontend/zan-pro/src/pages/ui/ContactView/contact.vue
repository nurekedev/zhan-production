<script>
import ToastNotificationComponent from '../../../shared/ToastNotificationComponent/toastNotificationComponent.vue';
import { computed, reactive, ref, toRefs } from 'vue';
import { useStore } from 'vuex';
    export default {
        name: "ContactPage",
        components: {
            ToastNotificationComponent,
        },
        setup() {
            // Data
            const store = useStore();
            const fields = reactive({
                full_name: '',
                phone_number: '',
                email: '',
                question_text: '',
            });
            const fieldRefs = toRefs(fields);
            const { full_name, phone_number, email, question_text } = fieldRefs;
            const toast = ref(null);
            // Computed
            const responseMessage = computed(() => store.getters.getMessage);

            // Methods
            // TODO: make regex validation for every input
            const validateName = () => {};
            const validatePhone = () => {};
            const validateEmail = () => {};
            const validateQuestionText = () => {};
            const handleSubmit = async () => {
                try {
                    const formValues = {
                        full_name: full_name.value,
                        phone_number: phone_number.value,
                        email: email.value,
                        question_text: question_text.value
                    }
                    await store.dispatch('questionSubmit', formValues);

                    console.log(phone_number.value, full_name.value, email.value, question_text.value);
                } catch (error) {
                    console.log(error);
                    throw error;
                }
            };
            const showToast = () => {
                toast.value.showToast();
            };
            
            return {
                ...fieldRefs,
                responseMessage,
                handleSubmit,
                toast,
                showToast
            }
        },
    }
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
                <form v-on:submit.prevent="handleSubmit()">
                    <p>{{ $t('contactsFormHeader') }}</p>
                    <div class="input-container">
                        <input type="text" name="name" id="name" placeholder="" v-model="full_name">
                        <label for="name">{{ $t('formLabelName') }}</label>
                    </div>
                    <div class="input-container">
                        <input type="tel" name="number" id="number" placeholder="" v-model="phone_number">
                        <label for="number">{{ $t('formLabelNumber') }}</label>
                    </div>
                    <div class="input-container">
                        <input type="email" name="email" id="email" placeholder="" v-model="email">
                        <label for="email">{{ $t('formLabelMail') }}</label>
                    </div>
                    <div class="input-container">
                        <textarea name="additional" id="additional" cols="30" rows="10" placeholder="" v-model="question_text"></textarea>
                        <label for="additional">{{ $t('formLabelOptional') }}</label>
                    </div>
                    <button type="submit" @click="showToast">{{ $t('formButton') }}</button>
                </form>
            </div>
        </article>
        <ToastNotificationComponent ref="toast" :message="responseMessage" />
    </main>
</template>