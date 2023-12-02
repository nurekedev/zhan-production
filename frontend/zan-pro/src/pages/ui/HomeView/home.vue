<script>
import ToastNotificationComponent from '../../../shared/ToastNotificationComponent/toastNotificationComponent.vue';
import { computed, reactive, ref, toRefs, onMounted, watch } from 'vue';
import { useStore } from 'vuex';
import { useI18n } from 'vue-i18n';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation, Pagination, Scrollbar, A11y, EffectFade } from 'swiper/modules';
import router from '../../../app/providers';
import 'swiper/scss';
import 'swiper/scss/navigation';
import 'swiper/scss/pagination';
import 'swiper/scss/autoplay';

// FIXME: remove unneсessary data(states)
export default {
    components: {
        ToastNotificationComponent,
        Swiper,
        SwiperSlide,
    },
    setup() {
        const { locale } = useI18n();
        const store = useStore();
        const form = reactive({
            full_name: '',
            phone_number: ''
        });
        const formRefs = toRefs(form);
        const { full_name, phone_number } = formRefs;
        const nameError = ref('');
        const phoneError = ref('');
        const message = ref('');
        const toast = ref(null);
        const emptyStringRegex = /^\s*$/;

        // Computed
        const responseMessage = computed(() => store.getters.getMessage);
        const errorMessage = computed(() => store.getters.errorMessage)
        const resStatus = computed(() => store.getters.responseStatus)
        const reviews = computed(() => store.getters.allReviews)

        // Methods
        const showToast = () => {
            toast.value.showToast();
        };
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
            // FIXME: Fix spaces between numbers in regex
            const phoneRegexPoland = /^(?:\+?48)?(?:\s?\d{3}\s?){3}$/;
            const phoneRegexKazakhstan = /^(?:\+?7|8)\s?\(?\d{3}\)?\s?\d{3}[-]?\d{2}[-]?\d{2}$/;
            const phoneRegexRussia = /^(?:\+?7|8)\s?\(?\d{3}\)?\s?\d{3}[-]?\d{2}[-]?\d{2}$/;
            if (
                phoneRegexPoland.test(phone_number.value) ||
                phoneRegexRussia.test(phone_number.value) || 
                phoneRegexKazakhstan.test(phone_number.value)
            ) {
                phoneError.value = 'The phone field must be filled!';
                return false;
            } else {
                phoneError.value = '';
                return true;
            }
        };
        const handleSubmit = async () => {
            // FIXME: trigger api request only when no errors
            validateName(full_name);
            validatePhone(phone_number);
            try {
                const formValues = {
                    full_name: full_name.value,
                    phone_number: phone_number.value,
                }
                await store.dispatch('submitForm', formValues);
            } catch (error) {
                if (resStatus === '500') {
                    router.push('/error500')
                }
                console.log(error);    
            }
        };

        onMounted(() => store.dispatch('fetchReviews', locale.value));
        watch(locale, async (newLocale, oldLocale) => {
            if (newLocale !== oldLocale) {
                store.dispatch('fetchReviews', locale.value);
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
            errorMessage,
            reviews,
            modules: [Navigation, Pagination, Scrollbar, A11y]
        }
    },
}
</script>

<template>
    <main class="home-main">
        <section>
            <img src="../../model/main.jpeg" />
            <div class="img-t-q">
                <article>
                    <h1>{{ $t('homePictureHeader') }}</h1>
                    <p>
                        {{ $t('homePictureText') }}
                    </p>
                </article>
                <div class="form-group">
                    <form v-on:submit.prevent="handleSubmit()">
                        <p>{{ $t('homeFormHeader') }}</p>
                        <div class="input-container">
                            <input type="text" name="name" id="name" placeholder="" v-model="full_name">
                            <label for="name">{{ $t('formLabelName') }}</label>
                            <span class="validation-error" v-if="nameError">{{ nameError }}</span>
                        </div>
                        <div class="input-container">
                            <input type="tel" name="phone" id="phone" placeholder="" v-model="phone_number">
                            <label for="phone">{{ $t('formLabelNumber') }}</label>
                            <span class="validation-error" v-if="phoneError">{{ phoneError }}</span>
                        </div>
                        <button @click="showToast" type="submit">{{ $t('formButton') }}</button>
                    </form>
                </div>
            </div>
        </section>
        <article>
            <div class="about">
                <h1>{{ $t('homeMainHeader') }}</h1>
                <p>
                    {{ $t('homeMainText') }}
                </p>
            </div>
            <Swiper
                :modules="modules"
                :pagination="{ clickable: true }"
                :autoplay="{ delay: 3000, disableOnInteraction: false }"
                navigation
            >
                <SwiperSlide v-for="review in reviews" :key="review.author">
                    <div class="review">
                        <h1>{{ $t('homeReviewHeader') }}</h1>
                        <img :src="review.author_pic" class="review-img">
                        <h2>{{ review.author }}</h2>
                        <p>
                            "{{ review.body_text }}"
                        </p>
                    </div>
                </SwiperSlide>
            </Swiper>
        </article>
        <ToastNotificationComponent v-if="responseMessage" ref="toast" :message="responseMessage" />
    </main>
</template>

<script>

</script>