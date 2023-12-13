<script>
    import ToastNotificationComponent from "../../../shared/ToastNotificationComponent/toastNotificationComponent.vue";
    import { computed, reactive, ref, toRefs } from "vue";
    import { useStore } from "vuex";
    export default {
        name: "ContactPage",
        components: {
            ToastNotificationComponent,
        },
        setup() {
            // Data
            const store = useStore();
            const fields = reactive({
                full_name: "",
                phone_number: "",
                email: "",
                question_text: "",
            });
            const fieldRefs = toRefs(fields);
            const { full_name, phone_number, email, question_text } = fieldRefs;
            const toast = ref(null);
            const errors = reactive({
                nameError: "",
                phoneError: "",
                emailError: "",
                questionError: "",
            });
            const errorRefs = toRefs(errors);
            const { nameError, phoneError, emailError, questionError } =
                errorRefs;
            // Computed
            const responseMessage = computed(() => store.getters.getMessage);
            const resStatus = computed(() => store.getters.responseStatus);

            // Methods
            // TODO: make regex validation for every input
            const validateName = () => {
                const emptyStringRegex = /^\s*$/;
                if (emptyStringRegex.test(question_text.value)) {
                    nameError.value = "Name field must be filled!";
                    return false;
                } else {
                    nameError.value = "";
                    return true;
                }
            };
            const validatePhone = () => {
                const phoneNumberPattern =
                    /\b\d{11,}\b|\+\d{1,}\(\d{3}\)\d{3}[\s-]?\d{4}|\+\d{2}\d{3}[\s-]?\d{3}[\s-]?\d{3}|\d{4}[\s-]?\d{3}[\s-]?\d{4}|\d{3}[\s-]?\d{4}[\s-]?\d{4}/;
                if (!phoneNumberPattern.test(phone_number.value)) {
                    phoneError.value =
                        "The phone format is incorrect! It must contain at least 11 numbers.";
                    return false;
                } else {
                    phoneError.value = "";
                    return true;
                }
            };
            const validateEmail = () => {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailPattern.test(email.value)) {
                    emailError.value = "The email format is incorrect!";
                    return false;
                } else {
                    emailError.value = "";
                    return true;
                }
            };
            const validateQuestionText = () => {
                const emptyStringRegex = /^\s*$/;
                if (emptyStringRegex.test(question_text.value)) {
                    questionError.value = "This field must be filled!";
                    return false;
                } else {
                    questionError.value = "";
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
                        
                        await store.dispatch("questionSubmit", formValues);


                        console.log(
                            phone_number.value,
                            full_name.value,
                            email.value,
                            question_text.value
                        );
                    } catch (error) {
                        if (resStatus === "500") {
                            router.push("/error500");
                        }
                        console.log(error);
                        throw error;
                    }
                } else {
                    store.dispatch("setMessage", "You filled wrond data!");
                }
            };
            const showToast = () => {
                toast.value.showToast();
            };

            return {
                ...fieldRefs,
                ...errorRefs,
                responseMessage,
                handleSubmit,
                toast,
                showToast,
            };
        },
    };
</script>

<template>
    <main class="contact">
        <section>
            <div>{{ $t("navContact") }}</div>
        </section>
        <article class="main-article">
            <div class="main-text">
                <p>{{ $t("contactsMainText") }}</p>
            </div>
            <div class="form-group">
                <form v-on:submit.prevent="handleSubmit()">
                    <p>{{ $t("contactsFormHeader") }}</p>
                    <div class="input-container">
                        <input
                            type="text"
                            name="name"
                            id="name"
                            placeholder=""
                            v-model="full_name"
                        />
                        <label for="name">{{ $t("formLabelName") }}</label>
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
                        <label for="number">{{ $t("formLabelNumber") }}</label>
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
                        <label for="email">{{ $t("formLabelMail") }}</label>
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
                            $t("formLabelOptional")
                        }}</label>
                        <span class="validation-error" v-if="questionError">{{
                            questionError
                        }}</span>
                    </div>
                    <button type="submit" @click="showToast">
                        {{ $t("formButton") }}
                    </button>
                </form>
            </div>
        </article>
        <ToastNotificationComponent ref="toast" :message="responseMessage" />
    </main>
</template>
