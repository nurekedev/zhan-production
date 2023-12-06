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
        const validateName = () => {
            if (emptyStringRegex.test(full_name.value)) {
                nameError.value = 'The name field must be filled!';
                return false;
            } else {
                nameError.value = '';
                return true;
            }
        };

        const validatePhone = () => {
            const globalPhoneRegex = /^(?:\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$/;
            // FIXME: WARNING FIX DISPLAYING THE ERROR
            if (!globalPhoneRegex.test(phone_number.value)) {
                phoneError.value = 'Please write valid number';
                return false;
            } else {
                phoneError.value = '';
                return true;
            }
        };

        const validateEmail = () => {
            const emailValue = emailField.value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (emailRegex.test(emailValue)) {
                emailError.value = ''; // Поле ошибки для email (предположим, что переменная emailError хранит информацию об ошибке)
                return true;
            } else {
                emailError.value = 'Invalid email format!'; // Сообщение об ошибке
                return false;
            }
        };

        const validateQuestionText = (questionText) => {
            if (!questionText.trim()) {
                // Если текст вопроса пуст или содержит только пробельные символы
                return false; // Возврат false, если текст пустой
            } else {
                return true; // Возврат true, если текст не пустой
            }
        };

        const handleSubmit = async () => {
            if (validateName() && validatePhone() && validateEmail() && validateQuestionText()) {
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
                        <textarea name="additional" id="additional" cols="30" rows="10" placeholder=""
                            v-model="question_text"></textarea>
                        <label for="additional">{{ $t('formLabelOptional') }}</label>
                    </div>
                    <button type="submit" @click="showToast">{{ $t('formButton') }}</button>
                </form>
            </div>
        </article>
        <ToastNotificationComponent ref="toast" :message="responseMessage" />
    </main>
</template>