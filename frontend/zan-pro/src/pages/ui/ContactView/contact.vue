<script>
    import ToastNotificationComponent from '../../../shared/ToastNotificationComponent/toastNotificationComponent.vue';
    import { computed, reactive, ref, toRefs, onMounted } from 'vue';
    import { useStore } from 'vuex';
    import { useI18n } from 'vue-i18n';
    export default {
        name: 'ContactPage',
        components: {
            ToastNotificationComponent,
        },
        setup() {
            // Data
            const { t, locale } = useI18n();
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
            const errors = reactive({
                nameError: '',
                phoneError: '',
                emailError: '',
                questionError: '',
            });
            const errorRefs = toRefs(errors);
            const { nameError, phoneError, emailError, questionError } =
                errorRefs;
            // Computed
            const fbUrl = computed(() => store.getters.getFb);
            const vkUrl = computed(() => store.getters.getVk);
            const igUrl = computed(() => store.getters.getIg);
            const xUrl = computed(() => store.getters.getX);
            const waUrl = computed(() => store.getters.getWa);
            const responseMessage = computed(() => store.getters.getMessage);
            const responseStatus = computed(() => store.getters.responseStatus);

            // Methods
            // TODO: make regex validation for every input
            const validateName = () => {
                const emptyStringRegex = /^\s*$/;
                if (emptyStringRegex.test(question_text.value)) {
                    nameError.value = t('formNameError');
                    return false;
                } else {
                    nameError.value = '';
                    return true;
                }
            };
            const validatePhone = () => {
                const phoneNumberPattern =
                    /\b\d{11,}\b|\+\d{1,}\(\d{3}\)\d{3}[\s-]?\d{4}|\+\d{2}\d{3}[\s-]?\d{3}[\s-]?\d{3}|\d{4}[\s-]?\d{3}[\s-]?\d{4}|\d{3}[\s-]?\d{4}[\s-]?\d{4}/;
                if (!phoneNumberPattern.test(phone_number.value)) {
                    phoneError.value = t('formPhoneError');
                    return false;
                } else {
                    phoneError.value = '';
                    return true;
                }
            };
            const validateEmail = () => {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailPattern.test(email.value)) {
                    emailError.value = t('formEmailError');
                    return false;
                } else {
                    emailError.value = '';
                    return true;
                }
            };
            const validateQuestionText = () => {
                const emptyStringRegex = /^\s*$/;
                if (emptyStringRegex.test(question_text.value)) {
                    questionError.value = t('formAddError');
                    return false;
                } else {
                    questionError.value = '';
                    return true;
                }
            };
            const handleSubmit = async () => {
                if (
                    validateName() &&
                    validatePhone() &&
                    validateEmail() &&
                    validateQuestionText()
                ) {
                    const formValues = {
                        full_name: full_name.value,
                        phone_number: phone_number.value,
                        email: email.value,
                        question_text: question_text.value,
                    };

                    try {
                        await store.dispatch('questionSubmit', formValues);

                        full_name.value = '';
                        phone_number.value = '';
                        email.value = '';
                        question_text.value = '';
                        store.dispatch('setMessage', t('form200'));
                    } catch (error) {
                        if (responseStatus.value === 500) {
                            router.push('/error500');
                        }
                        if (responseStatus.value === 429) {
                            store.dispatch('setMessage', t('form429'));
                        }
                        throw error;
                    }
                } else {
                    store.dispatch('setMessage', t('formWrongData'));
                }
            };
            const showToast = () => {
                toast.value.showToast();
            };

            // Life Cycle
            onMounted(async () => {
                await store.dispatch('getFbUrl');
                await store.dispatch('getIgUrl');
                await store.dispatch('getXUrl');
                await store.dispatch('getWaUrl');
            });

            return {
                ...fieldRefs,
                ...errorRefs,
                responseMessage,
                handleSubmit,
                toast,
                showToast,
                t,
                locale,
                fbUrl,
                vkUrl,
                igUrl,
                xUrl,
                waUrl,
            };
        },
    };
</script>

<template>
    <main class="contact">
        <section class="img">
            <div>{{ $t('navContact') }}</div>
        </section>
        <article class="main-article">
            <div class="main-text">
                <p>{{ $t('contactsMainText') }}</p>
                <div class="social-links">
                    <div class="mail">
                        <img src="../../model/email.svg" alt="" />
                        <a href="#"> <span>zhanarfraczak@gmail.com</span></a>
                    </div>
                    <div class="icons">
                        <a :href="fbUrl" target="_blank" v-if="fbUrl"
                            ><img src="../../model/facebook.svg" alt="facebook"
                        /></a>
                        <a :href="igUrl" target="_blank" v-if="igUrl"
                            ><img src="../../model/instagram.svg" alt=""
                        /></a>
                        <a :href="xUrl" target="_blank" v-if="xUrl"
                            ><img src="../../model/twiter.svg" alt=""
                        /></a>
                        <a :href="waUrl" target="_blank" v-if="waUrl"
                            ><img src="../../model/whatsapp.svg" alt=""
                        /></a>
                    </div>
                </div>
            </div>
            <div class="form-group">
                <form v-on:submit.prevent="handleSubmit()">
                    <p>{{ $t('contactsFormHeader') }}</p>
                    <div class="input-container">
                        <input
                            type="text"
                            name="name"
                            id="name"
                            placeholder=""
                            v-model="full_name"
                        />
                        <label for="name">{{ $t('formLabelName') }}</label>
                        <span class="validation-error" v-if="nameError">{{
                            nameError
                        }}</span>
                    </div>
                    <div class="input-container">
                        <input
                            type="tel"
                            name="number"
                            id="number"
                            placeholder=""
                            v-model="phone_number"
                        />
                        <label for="number">{{ $t('formLabelNumber') }}</label>
                        <span class="validation-error" v-if="phoneError">{{
                            phoneError
                        }}</span>
                    </div>
                    <div class="input-container">
                        <input
                            type="email"
                            name="email"
                            id="email"
                            placeholder=""
                            v-model="email"
                        />
                        <label for="email">{{ $t('formLabelMail') }}</label>
                        <span class="validation-error" v-if="emailError">{{
                            emailError
                        }}</span>
                    </div>
                    <div class="input-container">
                        <textarea
                            name="additional"
                            id="additional"
                            cols="30"
                            rows="10"
                            placeholder=""
                            v-model="question_text"
                        ></textarea>
                        <label for="additional">{{
                            $t('formLabelOptional')
                        }}</label>
                        <span class="validation-error" v-if="questionError">{{
                            questionError
                        }}</span>
                    </div>
                    <section class="policy-container">
                        <p class="policy">
                            {{ $t('formPolicyPart1') }}
                            <router-link to="/policy"
                                ><a>
                                    {{ $t('formPolicyPart2') }}
                                </a>
                            </router-link>
                        </p>
                    </section>
                    <button type="submit" @click="showToast">
                        {{ $t('formButton') }}
                    </button>
                </form>
            </div>
        </article>
        <ToastNotificationComponent ref="toast" :message="responseMessage" />
    </main>
</template>
