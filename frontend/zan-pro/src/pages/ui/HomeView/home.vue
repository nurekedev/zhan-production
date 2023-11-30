<script>
import ToastNotificationComponent from '../../../shared/ToastNotificationComponent/toastNotificationComponent.vue';
import { computed, reactive, ref, toRefs } from 'vue';
import { useStore } from 'vuex';

// FIXME: remove unneсessary data(states)
export default {
    components: {
        ToastNotificationComponent
    },
    setup() {
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

        const responseMessage = computed(() => store.getters.getMessage);
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
            // const phoneRegexPoland = /^(?:\+?48)?(?:\s?\d{3}\s?){3}$/;
            // const phoneRegexKazakhstan = /^(?:\+?7|8)\s?\(?\d{3}\)?\s?\d{3}[-]?\d{2}[-]?\d{2}$/;
            // const phoneRegexRussia = /^(?:\+?7|8)\s?\(?\d{3}\)?\s?\d{3}[-]?\d{2}[-]?\d{2}$/;
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
            // validateName(full_name);
            // validatePhone(phone_number);
            try {
                const formValues = {
                    full_name: full_name.value,
                    phone_number: phone_number.value,
                }
                await store.dispatch('submitForm', formValues);

                console.log(phone_number.value, full_name.value);
            } catch (error) {
                console.log(error);    
            }
        };

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
        }
    },
    // data() {
    //     return {
    //         form: {
    //             full_name: '',
    //             phone_number: '',
    //         },
    //         message: '',
    //         error: [

    //         ]
    //     }
    // },
    // methods: {
    //     showToast() {
    //         this.$refs.toast.showToast();
    //     },
    //     submitLightForm() {
    //         console.log("submit form", this.form)
            
    //         this.errors = []
            
    //         if (this.form.full_name === '') {
    //             this.errors.push('The name must be filled out')
    //         }
            
    //         if (this.form.phone_number === '') {
    //             this.errors.push('The content must be filled out')
    //         }

    //         if(!this.error.lenght) {
    //         // const csrftoken = getCSRFToken();
    //             axios
    //                 .post(`${this.$i18n.locale}/submit-contact/`, this.form)
    //                 .then(response => {
    //                     this.form.full_name = ''
    //                     this.form.phone_number = ''
                        
    //                     this.message = response.data.message;
    //                     this.$emit('submitLightForm', response.data)
    //                 })
    //                 .catch(error => {
    //                     console.log(error)
    //                 })
    //         }
    //     }
    // }
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
                        <!-- <input type="text" placeholder="Имя" v-model="full_name">
                        <input type="tel" pattern="[0-9]{11}" placeholder="Телефон" v-model="phone_number"> -->
                        <!-- <p class="error" v-for="error in errors" v-bind:key="error">{{ error }}</p> -->
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
            <!-- TODO: Carousel animation -->
            <aside>
                <div class="review-title">
                    <h1>{{ $t('homeReviewHeader') }}</h1>
                    <img class="review-img">
                    <h2>Динара Асылхановна</h2>
                    <p>
                        "{{ $t('homeReviewText') }}"
                    </p>
                    <div class="home-pagination">
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            </aside>
        </article>
        <ToastNotificationComponent ref="toast" :message="responseMessage" />
    </main>
</template>

<script>

</script>