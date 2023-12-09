<script>
    import { ref } from "vue";
    import { useStore } from "vuex";
    import { reactive, toRefs, computed, onMounted, watch } from "vue";
    import EmpItemComponent from "../../../widgets/ui/EmpItemComponent/EmpItemComponent.vue";
    import ToastNotificationComponent from "../../../shared/ToastNotificationComponent/toastNotificationComponent.vue";
    import { useI18n } from "vue-i18n";
    import { watchEffect } from "vue";
    export default {
        name: "VacancyPage",
        components: {
            EmpItemComponent,
            ToastNotificationComponent,
        },
        props: ["slug"],
        setup(props) {
            // State
            const { t, locale } = useI18n();
            const store = useStore();
            const showModal = ref(false);
            const selectedFileName = ref("");
            const fileInput = ref(null);
            const fields = reactive({
                full_name: "",
                phone_number: "",
                email: "",
                cv_field: null,
                additional_text: "",
            });
            const fieldRefs = toRefs(fields);
            const {
                full_name,
                phone_number,
                email,
                cv_field,
                additional_text,
            } = fieldRefs;
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
            const currentVacancy = computed(() => store.getters.currentVacancy);
            const similarVacancies = computed(
                () => store.getters.allSimilarVacancies
            );
            const responseMessage = computed(() => store.getters.getMessage);
            console.log(currentVacancy.value);

            // Methods
            const openModal = () => (showModal.value = true);
            const closeModal = () => (showModal.value = false);
            const onFileChange = (event) => {
                const file = event.target.files[0];
                if (file) {
                    const start = file.name.lastIndexOf(".");
                    const format = file.name.slice(start + 1, file.name.length);
                    if (format === "png" || format === "pdf") {
                        selectedFileName.value = file.name;
                        console.log(selectedFileName.value);
                    } else {
                        store.dispatch("setMessage", t("formFileError"));
                        showToast();
                    }
                } else {
                    selectedFileName.value = "";
                }
            };
            const validateName = () => {
                const emptyStringRegex = /^\s*$/;
                if (emptyStringRegex.test(full_name.value)) {
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
                if (emptyStringRegex.test(full_name.value)) {
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
                    const formData = new FormData();
                    formData.append("full_name", full_name.value);
                    formData.append("phone_number", phone_number.value);
                    formData.append("email", email.value);
                    formData.append("cv_field", fileInput.value.files[0]);
                    formData.append("additional_text", additional_text.value);
                    try {
                        store.dispatch("submitVacancy", {
                            slug: props.slug,
                            form: formData,
                        });
                        full_name.value = "";
                        phone_number.value = "";
                        email.value = "";
                        fileInput.value = null;
                        additional_text.value = "";
                        showToast();
                    } catch (e) {
                        if (resStatus === "500") {
                            router.push("/error500");
                        }
                        console.log(e);
                        throw e;
                    }
                } else {
                    store.dispatch("setMessage", "You filled wrond data!");
                }
            };
            const showToast = () => {
                showModal.value = false;
                if (responseMessage.value) {
                    toast.value.showToast();
                }
            };

            onMounted(() =>
                store.dispatch("fetchVacancy", {
                    locale: locale.value,
                    slug: props.slug,
                })
            );

            watchEffect(() =>
                store.dispatch("fetchVacancy", {
                    locale: locale.value,
                    slug: props.slug,
                })
            );

            watch(locale, async (newLocale, oldLocale) => {
                if (newLocale !== oldLocale) {
                    await store.dispatch("fetchVacancies", locale.value);
                }
            });

            return {
                ...fieldRefs,
                ...errorRefs,
                showModal,
                selectedFileName,
                openModal,
                closeModal,
                onFileChange,
                currentVacancy,
                similarVacancies,
                fileInput,
                handleSubmit,
                toast,
                responseMessage,
                showToast,
                // vacancyItem
            };
        },
    };
</script>

<template>
    <main class="main-page">
        <div class="main-img">
            <div class="info">
                <p>{{ $t("navWork") }}</p>
            </div>
        </div>
        <div class="left-side">
            <section class="top-container">
                <div class="left-info">
                    <h2>{{ currentVacancy.name }}</h2>
                    <p class="salary">
                        {{ $t("vacancySalary") }}:
                        <span>{{ currentVacancy.salary }} $</span>
                    </p>
                </div>
                <div class="right-info">
                    <div class="right-info__text">
                        <p>{{ currentVacancy.company.name }}</p>
                        <p class="city">{{ currentVacancy.city.name }}</p>
                    </div>
                    <button @click="openModal">
                        {{ $t("vacancyRespond") }}
                    </button>
                </div>
            </section>
            <article class="details">
                <section
                    v-if="currentVacancy.responsibility_text"
                    class="detail responsibilities"
                >
                    <h4>{{ $t("vacancyResponsibility") }}</h4>
                    <p>{{ currentVacancy.responsibility_text }}</p>
                </section>

                <section
                    v-if="currentVacancy.requirement_text"
                    class="detail responsibilities"
                >
                    <h4>{{ $t("vacancyRequirments") }}</h4>
                    <p>{{ currentVacancy.requirement_text }}</p>
                </section>

                <section
                    v-if="currentVacancy.schedule"
                    class="detail responsibilities"
                >
                    <h4>{{ $t("vacancySchedule") }}</h4>
                    <p>{{ currentVacancy.schedule }}</p>
                </section>

                <section
                    v-if="currentVacancy.working_condition_text"
                    class="detail requirments"
                >
                    <h4>{{ $t("vacancyCondition") }}</h4>
                    <p>{{ currentVacancy.working_condition_text }}</p>
                </section>

                <section
                    v-if="currentVacancy.accommodation"
                    class="detail living"
                >
                    <h4>{{ $t("vacancyLiving") }}</h4>
                    <p>{{ currentVacancy.accommodation }}</p>
                </section>

                <section
                    v-if="currentVacancy.nutrition"
                    class="detail schedule"
                >
                    <h4>{{ $t("vacancyNutrition") }}</h4>
                    <p>{{ currentVacancy.nutrition }}</p>
                </section>

                <section
                    v-if="currentVacancy.additional_text"
                    class="detail additional"
                >
                    <h4>{{ $t("vacancyAdditional") }}</h4>
                    <p>{{ currentVacancy.additional_text }}</p>
                </section>
            </article>
        </div>
        <aside class="similar-vacancy">
            <h2>{{ $t("vacancyAsideSimilar") }}</h2>
            <EmpItemComponent
                v-for="vacancy in similarVacancies"
                :key="vacancy.slug"
                :slug="vacancy.slug"
                :title="vacancy.name"
                :picURL="vacancy.model_pic"
                :salary="vacancy.salary"
                :companyName="vacancy.company.name"
                :city="vacancy.city.name"
            />
        </aside>
        <div class="modal-overlay" v-if="showModal" @click="closeModal"></div>
        <div class="modal" v-if="showModal">
            <div class="modal-content">
                <img
                    src="../../model/xmark.svg"
                    alt="X"
                    class="xmark"
                    @click="closeModal"
                />
                <form v-on:submit.prevent="handleSubmit">
                    <p>{{ $t("vacancyFormHeader") }}</p>
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
                            type="text"
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
                    <div class="input-container-file">
                        <input
                            @change="onFileChange"
                            ref="fileInput"
                            type="file"
                            name="file"
                            id="file"
                            placeholder=""
                            accept="image/png, image/jpg, image/jpeg, application/pdf"
                        />
                        <label class="input-file-label" for="file">{{
                            $t("formLabelFile")
                        }}</label>
                        <p v-if="selectedFileName" class="file-name">
                            {{ selectedFileName }}
                        </p>
                    </div>
                    <div class="input-container">
                        <textarea
                            name="additional"
                            id="additional"
                            cols="30"
                            rows="10"
                            placeholder=""
                            v-model="additional_text"
                        ></textarea>
                        <label for="additional">{{
                            $t("formLabelOptional")
                        }}</label>
                        <span class="validation-error" v-if="questionError">{{
                            questionError
                        }}</span>
                    </div>
                    <button type="submit">{{ $t("formButton") }}</button>
                </form>
            </div>
        </div>
        <ToastNotificationComponent ref="toast" :message="responseMessage" />
    </main>
</template>
