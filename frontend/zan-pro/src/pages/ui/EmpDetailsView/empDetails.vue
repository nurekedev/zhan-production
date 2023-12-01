<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import EmpItemComponent from '../../../widgets/ui/EmpItemComponent/EmpItemComponent.vue';
import { computed } from 'vue';
import { reactive } from 'vue';
import { onMounted } from 'vue';
    export default {
        name: 'VacancyPage',
        components: { EmpItemComponent },
        props: ["slug"],
        setup(props) {
            // State
            const store = useStore();
            const showModal = ref(false);
            const selectedFileName = ref('');

            // Computed
            const currentVacancy = computed(() => store.getters.currentVacancy);
            const similarVacancies = computed(() => store.getters.allSimilarVacancies);
            console.log(similarVacancies);

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

            onMounted(() => store.dispatch('fetchVacancy', props.slug))

            return {
                showModal,
                selectedFileName,
                openModal,
                closeModal,
                onFileChange,
                currentVacancy,
                similarVacancies,
                // vacancyItem
            }
        }
    }
</script>

<template>
    <main class="main-page" >
        <section>
            <img src="../../model/employment-main.jpeg" alt="emplloyment-main">
            <div class="info">
                <p>{{ $t('navWork') }}</p>
            </div>
        </section>
        <div class="left-side">
            <section class="top-container">
                <div class="left-info">
                    <h2>{{ currentVacancy.name }}</h2>
                    <p class="salary">Зарплата: <span>{{ currentVacancy.salary }} $</span><br><small>На руки</small></p>
                    <p>Без опыта работы</p>
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
                <form action="" method="post">
                        <p>{{ $t('vacancyFormHeader') }}</p>
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
                        <div class="input-container-file">
                            <input @change="onFileChange" ref="fileInput" type="file" name="file" id="file" placeholder="" accept="image/png, image/jpg, image/jpeg, application/pdf">
                            <label class="input-file-label" for="file">{{ $t('formLabelFile') }}</label>
                            <p v-if="selectedFileName" class="file-name">{{ selectedFileName }}</p>
                        </div>
                        <div class="input-container">
                            <textarea name="additional" id="additional" cols="30" rows="10" placeholder=""></textarea>
                            <label for="additional">{{ $t('formLabelOptional') }}</label>
                        </div>
                        <button type="submit">{{ $t('formButton') }}</button>
                </form>
            </div>
        </div>
    </main>
</template>