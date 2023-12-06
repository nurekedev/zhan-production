<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import { reactive, toRefs, computed, onMounted } from 'vue';
import EmpItemComponent from '../../../widgets/ui/EmpItemComponent/EmpItemComponent.vue';
import ToastNotificationComponent from '../../../shared/ToastNotificationComponent/toastNotificationComponent.vue';
    export default {
        name: 'VacancyPage',
        components: {
            EmpItemComponent,
            ToastNotificationComponent,
        },
        props: ["slug"],
        setup(props) {
            // State
            const store = useStore();
            const showModal = ref(false);
            const selectedFileName = ref('');
            const fileInput = ref(null);
            const fields = reactive({
                full_name: '',
                phone_number: '',
                email: '',
                cv_field: null,
                additional_text: '',
            });
            const fieldRefs = toRefs(fields);
            const { full_name, phone_number, email, cv_field, additional_text } = fieldRefs;
            const toast = ref(null);

            // Computed
            const currentVacancy = computed(() => store.getters.currentVacancy);
            const similarVacancies = computed(() => store.getters.allSimilarVacancies);
            const responseMessage = computed(() => store.getters.getMessage);

            // Methods
            const openModal = () => showModal.value = true;
            const closeModal = () => showModal.value = false;
            const onFileChange = (event) => {
                const file = event.target.files[0];
                if (file) {
                    selectedFileName.value = file.name;
                } else {
                    selectedFileName.value = '';
                }
            };
            const handleSubmit = async () => {
                const formData = new FormData();
                formData.append('full_name', full_name.value);
                formData.append('phone_number', phone_number.value);
                formData.append('email', email.value);
                formData.append('cv_field', fileInput.value.files[0]);
                formData.append('additional_text', additional_text.value);
                try {
                    store.dispatch('submitVacancy', {
                        slug: props.slug,
                        form: formData,
                    });
                    full_name.value = '';
                    phone_number.value = '';
                    email.value = '';
                    fileInput.value = null;
                    additional_text.value = '';
                    showToast();
                } catch (e) {
                    console.log(e);
                    throw e;
                }
            };
            const showToast = () => {
                showModal.value = false;
                if (responseMessage.value) {
                    toast.value.showToast();
                }
            };

            onMounted(() => store.dispatch('fetchVacancy', props.slug))

            return {
                ...fieldRefs,
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
            }
        }
    }
</script>

<template>
    <main class="main-page" >
        <div class="main-img">
            <div class="info">
                <p>{{ $t('navWork') }}</p>
            </div>
        </div>
        <div class="left-side">
            <section class="top-container">
                <div class="left-info">
                    <h2>{{ currentVacancy.name }}</h2>
                    <p class="salary">Зарплата: <span>{{ currentVacancy.salary }} $</span></p>
                </div>
                <div class="right-info">
                    <div class="right-info__text">
                        <p>{{ currentVacancy.company.name }}</p>
                        <p class="city">{{ currentVacancy.city.name }}</p>
                    </div>
                    <button @click="openModal">{{ $t('cardButtonRespond') }}</button>
                </div>
            </section>
            <article class="details">
                <section v-if="currentVacancy.responsibility_text" class="detail responsibilities">
                    <h4>{{ $t('vacancyResponsibility') }}</h4>
                    <p>{{ currentVacancy.responsibility_text }}</p>
                </section>
                <section v-if="currentVacancy.working_condition_text" class="detail requirments">
                    <h4>{{ $t('vacancyRequirments') }}</h4>
                    <p>{{ currentVacancy.working_condition_text }}</p>
                </section>
                <!-- <section class="detail schedule">
                    <h4>{{ $t('vacancySchedule') }}</h4>
                    <p></p>
                </section> -->
                <section v-if="currentVacancy.additional_text" class="detail additional">
                    <h4>{{ $t('vacancyAdditional') }}</h4>
                    <p>{{ currentVacancy.additional_text }}</p>
                </section>
                <section v-if="currentVacancy.accommodation" class="detail living">
                    <h4>{{ $t('vacancyLiving') }}</h4>
                    <p>{{ currentVacancy.accommodation }}</p>
                </section>
            </article>
        </div>
        <aside class="similar-vacancy">
            <h2>{{ $t('vacancyAsideSimilar') }}</h2>
            <EmpItemComponent
                v-for="vacancy in similarVacancies" :key="vacancy.slug"
                :slug="vacancy.slug"
                :title="vacancy.name"
                :picURL="vacancy.model_pic"
                :salary="vacancy.salary"
                :companyName="vacancy.company.name"
                :city="vacancy.city.name"
            />
        </aside>
        <div class="modal-overlay" v-if="showModal"></div>
        <div class="modal" v-if="showModal">
            <div class="modal-content">
                <img src="../../model/xmark.svg" alt="X" class="xmark" @click="closeModal">
                <form v-on:submit.prevent="handleSubmit">
                        <p>{{ $t('vacancyFormHeader') }}</p>
                        <div class="input-container">
                            <input type="text" name="name" id="name" placeholder="" v-model="full_name">
                            <label for="name">{{ $t('formLabelName') }}</label>
                        </div>
                        <div class="input-container">
                            <input type="text" name="number" id="number" placeholder="" v-model="phone_number">
                            <label for="number">{{ $t('formLabelNumber') }}</label>
                        </div>
                        <div class="input-container">
                            <input type="email" name="email" id="email" placeholder="" v-model="email">
                            <label for="email">{{ $t('formLabelMail') }}</label>
                        </div>
                        <div class="input-container-file">
                            <input @change="onFileChange" ref="fileInput" type="file" name="file" id="file" placeholder="" accept="image/png, image/jpg, image/jpeg, application/pdf">
                            <label class="input-file-label" for="file">{{ $t('formLabelFile') }}</label>
                            <p v-if="selectedFileName" class="file-name">{{ selectedFileName }}</p>
                        </div>
                        <div class="input-container">
                            <textarea name="additional" id="additional" cols="30" rows="10" placeholder="" v-model="additional_text"></textarea>
                            <label for="additional">{{ $t('formLabelOptional') }}</label>
                        </div>
                        <button type="submit">{{ $t('formButton') }}</button>
                </form>
            </div>
        </div>
        <ToastNotificationComponent ref="toast" :message="responseMessage" />
    </main>
</template>