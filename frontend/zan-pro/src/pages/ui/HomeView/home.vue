<script>
    import ToastNotificationComponent from "../../../shared/ToastNotificationComponent/toastNotificationComponent.vue";
    import { computed, reactive, ref, toRefs, onMounted, watch } from "vue";
    import { useStore } from "vuex";
    import { useI18n } from "vue-i18n";
    import { Swiper, SwiperSlide } from "swiper/vue";
    import { Navigation, Pagination, Scrollbar, A11y } from "swiper/modules";
    import router from "../../../app/providers";
    import "swiper/scss";
    import "swiper/scss/navigation";
    import "swiper/scss/pagination";
    import "swiper/scss/autoplay";

    export default {
        components: {
            ToastNotificationComponent,
            Swiper,
            SwiperSlide,
        },
        setup() {
            const { t, locale } = useI18n();
            const store = useStore();
            const form = reactive({
                full_name: "",
                phone_number: "",
            });
            const formRefs = toRefs(form);
            const { full_name, phone_number } = formRefs;
            const nameError = ref("");
            const phoneError = ref("");
            const message = ref("");
            const toast = ref(null);
            const emptyStringRegex = /^\s*$/;

            // Computed
            const responseMessage = computed(() => store.getters.getMessage);
            const resStatus = computed(() => store.getters.responseStatus);
            const reviews = computed(() => store.getters.allReviews);

            // Methods
            const showToast = () => {
                toast.value.showToast();
            };
            const validateName = () => {
                if (emptyStringRegex.test(full_name.value)) {
                    nameError.value = t("formNameError");
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
                    phoneError.value = t("formPhoneError");
                    return false;
                } else {
                    phoneError.value = "";
                    return true;
                }
            };
            const handleSubmit = async () => {
                if (validateName() && validatePhone()) {
                    try {
                        const formValues = {
                            full_name: full_name.value,
                            phone_number: phone_number.value,
                        };
                        await store.dispatch("submitForm", formValues);
                        full_name.value = "";
                        phone_number.value = "";
                    } catch (error) {
                        if (resStatus === 500) {
                            router.push("/error500");
                        }
                    }
                } else {
                    store.dispatch("setMessage", t("formWrongData"));
                }
            };

            onMounted(() => store.dispatch("fetchReviews", locale.value));
            // checks locale changing and triggers on change
            watch(locale, async (newLocale, oldLocale) => {
                if (newLocale !== oldLocale) {
                    store.dispatch("fetchReviews", locale.value);
                }
            });

            return {
                toast,
                full_name,
                nameError,
                phone_number,
                phoneError,
                message,
                showToast,
                handleSubmit,
                responseMessage,
                reviews,
                modules: [Navigation, Pagination, Scrollbar, A11y],
            };
        },
    };
</script>

<template>
    <main class="home-main">
        <section>
            <img src="../../model/main.jpeg" />
            <div class="img-t-q">
                <article>
                    <h1>{{ $t("homeMainHeader") }}</h1>
                    <p>
                        {{ $t("homeMainText") }}
                    </p>
                </article>
                <div class="form-group">
                    <form v-on:submit.prevent="handleSubmit()">
                        <p>{{ $t("homeFormHeader") }}</p>
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
                                name="phone"
                                id="phone"
                                placeholder=""
                                v-model="phone_number"
                            />
                            <label for="phone">{{
                                $t("formLabelNumber")
                            }}</label>
                            <span class="validation-error" v-if="phoneError">{{
                                phoneError
                            }}</span>
                        </div>
                        <section class="policy-container">
                            <p class="policy">
                                {{ $t("formPolicyPart1") }}
                                <router-link to="/policy"
                                    ><a>
                                        {{ $t("formPolicyPart2") }}
                                    </a>
                                </router-link>
                            </p>
                        </section>
                        <button @click="showToast" type="submit">
                            {{ $t("formButton") }}
                        </button>
                    </form>
                </div>
            </div>
        </section>
        <article>
            <!-- <div class="about">
                <h1>{{ $t("homeMainHeader") }}</h1>
                <p>
                    {{ $t("homeMainText") }}
                </p>
            </div> -->
            <!-- <Swiper
                :modules="modules"
                :pagination="{ clickable: true }"
                :autoplay="{ delay: 3000, disableOnInteraction: false }"
                navigation
            >
                <SwiperSlide v-for="review in reviews" :key="review.author">
                    <div class="review">
                        <h1>{{ $t("homeReviewHeader") }}</h1>
                        <img :src="review.author_pic" class="review-img" />
                        <h2>{{ review.author }}</h2>
                        <p>"{{ review.body_text }}"</p>
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 480 131"
                            fill="none"
                        >
                            <path
                                d="M273.148 61.3019C277.892 61.897 282.692 60.7729 286.678 58.1335L368.791 3.76616C374.247 0.153534 381.126 -0.561347 387.208 1.85203L480 38.669V130.5H0V38.669L49.2536 33.7255C50.7465 33.5756 52.2514 33.5943 53.7401 33.781L273.148 61.3019Z"
                                fill="#5AAAFA"
                                fill-opacity="0.1"
                            />
                        </svg>
                    </div>
                </SwiperSlide>
            </Swiper> -->
        </article>
        <ToastNotificationComponent ref="toast" :message="responseMessage" />
    </main>
</template>

<script></script>
