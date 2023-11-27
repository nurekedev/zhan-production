<script>
import axios from 'axios';

export default {
    data() {
        return {
            form: {
                full_name: '',
                phone_number: '',
            },
            error: [

            ]
        }
    },
    methods: {
        submitLightForm() {
            console.log("submit form", this.form)

            this.errors = []

            if (this.form.full_name === '') {
                this.errors.push('The name must be filled out')
            }

            if (this.form.phone_number === '') {
                this.errors.push('The content must be filled out')
            }

            if(!this.error.lenght) {
                axios
                    .post(`en/submit-contact/`, this.form)
                    .then(response => {
                        this.form.full_name = ''
                        this.form.phone_number = ''

                        this.$emit('submitLightForm', response.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
}
</script>

<template>
    <main class="home-main">
        <section>
            <img src="../../model/main.jpeg" />
            <div class="img-t-q">
                <article>
                    <h1>Работа в Польше</h1>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt ut labore et dolore 
                        magna aliqua. Auctor elit sed vulputate mi.
                    </p>
                </article>
                <form v-on:submit.prevent="submitLightForm()">
                    <label>Уточните что вы хотите?</label>
                    <input type="text" placeholder="Имя" v-model="form.full_name">
                    <input type="tel" pattern="[0-9]{11}" placeholder="Телефон" v-model="form.phone_number">
                    <p class="error" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    <button type="submit">Отправить</button>
                </form>
            </div>
        </section>
        <article>
            <div class="about">
                <h1>О компании</h1>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Auctor elit sed vulputate mi. Faucibus scelerisque
                    eleifend donec pretium vulputate sapien nec sagittis aliquam.
                    At tempor commodo ullamcorper a lacus vestibulum sed arcu non.
                    Amet purus gravida quis blandit. Scelerisque purus semper eget
                    duis at tellus at urna condimentum. Et malesuada fames ac turpis egestas maecenas. 
                </p>
            </div>
            <aside>
                <div class="review-title">
                    <h1>Отзывы клиентов</h1>
                    <img class="review-img">
                    <h2>Динара Асылхановна</h2>
                    <p>
                        "Share a real testimonial that hits some of your benefits (but isn’t too sales-y)."
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
    </main>
</template>

