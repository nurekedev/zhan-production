<script>
    export default {
        data() {
            return {
                showModal: false,
            }
        },
        methods: {
            openModal() {
                this.showModal = true;
            },
            closeModal() {
                this.showModal = false;
            }
        },
    }
</script>

<template>
    <main class="main-page" >
        <section>
            <img src="../../model/employment-main.jpeg" alt="emplloyment-main">
            <div class="info">
                <p>Трудоустройство в Польше</p>
            </div>
        </section>
        <div class="left-side">
            <section class="top-container">
                <div class="left-info">
                    <h2>UX/UI Designer</h2>
                    <p class="salary">Зарплата: <span>1000 - 1500 $</span><br><small>На руки</small></p>
                    <p>Без опыта работы</p>
                </div>
                <div class="right-info">
                    <div class="right-info__text">
                        <p>Частная компаия %Company Name%</p>
                        <p class="city">Варшава</p>
                    </div>
                    <button @click="openModal">Откликнуться</button>
                </div>
            </section>
            <article class="details">
                <section class="detail description">
                    <h4>Описание</h4>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex officiis labore molestiae! Sed laborum ipsam officiis iure ea laudantium vel!</p>
                    <ul>
                        <li><p>Lorem, ipsum dolor.</p></li>
                        <li><p>Lorem, ipsum dolor.</p></li>
                        <li><p>Lorem, ipsum dolor.</p></li>
                        <li><p>Lorem, ipsum dolor.</p></li>
                    </ul>
                </section>
                <section class="detail responsibilities">
                    <h4>Обязанности</h4>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro molestiae, quidem culpa magnam minima blanditiis. Excepturi, vitae odio voluptatum fugiat iure, ut quod dolorem at exercitationem harum dolor laborum voluptas, itaque velit possimus repellat ab ipsa repudiandae laboriosam. Quae numquam eius ducimus excepturi suscipit voluptates animi eligendi illo itaque eum!</p>
                </section>
                <section class="detail requirments">
                    <h4>Требования</h4>
                    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt ex laborum amet quo sed accusantium ratione reprehenderit minus aliquam est tempore illo iste eius non, doloribus dolores vel aperiam quasi iure, at, ea quidem id. Doloribus, voluptatem rem. Et eos necessitatibus neque nobis architecto voluptate repudiandae alias distinctio incidunt fugiat quos rerum saepe a dolorem, ab deserunt. At dignissimos et veritatis aperiam cumque? Saepe dolores ducimus atque beatae, velit commodi aliquid placeat pariatur voluptatem, necessitatibus est harum neque nesciunt, exercitationem sapiente laborum natus dolor et nam sit libero tempora. Dolores aut voluptas perspiciatis reiciendis ut quo architecto omnis molestias nisi!</p>
                </section>
                <section class="detail schedule">
                    <h4>График работы</h4>
                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Suscipit neque, explicabo a maxime reiciendis libero quia! Officiis sit cupiditate velit est ex nostrum asperiores obcaecati veniam. Saepe, minima eveniet quo officia labore, vitae asperiores nihil natus sapiente dolorum eius id repellendus, dolores placeat laboriosam exercitationem nesciunt! Omnis id voluptatibus officiis nemo eligendi, harum cum asperiores commodi eos minus earum ab reiciendis recusandae, ipsam, corporis velit rem delectus! Earum quibusdam recusandae numquam fugiat a dolores fuga repudiandae rerum eum explicabo, quia porro esse at non suscipit quis impedit dolorum dignissimos, accusantium, exercitationem minima excepturi! Blanditiis molestiae nesciunt nihil rerum, sint nam.</p>
                </section>
                <section class="detail additional">
                    <h4>Дополнительно</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quasi, voluptas amet maxime pariatur excepturi eaque! Reprehenderit tempore nostrum deleniti veritatis quae recusandae commodi corrupti dicta quis reiciendis? Ipsum doloremque quisquam sunt animi voluptates quo laboriosam numquam reprehenderit mollitia iste incidunt repellat labore possimus, quidem dignissimos odit temporibus officiis optio dolor laudantium, illo dolore nam? Impedit repudiandae sit, laboriosam est culpa at illo voluptatibus optio inventore consequuntur officiis totam reiciendis dicta. </p>
                </section>
                <section class="detail living">
                    <h4>Проживание</h4>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint fugiat iste iure aspernatur quia alias beatae molestias corrupti mollitia molestiae dolore, nisi, qui, vel accusamus animi ipsa neque eveniet doloribus. Harum sequi excepturi consequuntur culpa repellendus libero quae mollitia reiciendis, assumenda, labore, expedita perspiciatis magni porro ducimus fuga quaerat veniam!</p>
                </section>
            </article>
        </div>
        <aside class="similar-vacancy">
            <h2>Вакансии в том же городе</h2>
            <div class="item">
                <img src="../../model/Vacancy img.png">
                <article>
                    <h1>UX/UI designer</h1>
                    <h2>1000$</h2>
                    <h3>Частная компания “Company Name”</h3>
                    <h3>Варшава</h3>
                    <div class="btn">
                        <button><router-link to="/employmentDetails">Откликнуться</router-link></button>
                        <button><router-link to="/contact">Показать контакты</router-link></button>
                    </div>
                </article>
            </div>
            <div class="item">
                <img src="../../model/Vacancy img.png">
                <article>
                    <h1>UX/UI designer</h1>
                    <h2>1000$</h2>
                    <h3>Частная компания “Company Name”</h3>
                    <h3>Варшава</h3>
                    <div class="btn">
                        <button><router-link to="/employmentDetails">Откликнуться</router-link></button>
                        <button><router-link to="/contact">Показать контакты</router-link></button>
                    </div>
                </article>
            </div>
        </aside>
        <div class="modal-overlay" v-if="showModal"></div>
        <div class="modal" v-if="showModal">
            <div class="modal-content">
                <span class="xmark" @click="closeModal">X</span>
                <form action="" method="post">
                        <p>Оставить заявку</p>
                        <div class="input-container">
                            <input type="text" name="name" id="name" placeholder="">
                            <label for="name">Имя</label>
                        </div>
                        <div class="input-container">
                            <input type="text" name="number" id="number" placeholder="">
                            <label for="number">Телефон</label>
                        </div>
                        <div class="input-container">
                            <input type="email" name="email" id="email" placeholder="">
                            <label for="email">E-mail</label>
                        </div>
                        <div class="input-container-file">
                            <input type="file" name="file" id="file" placeholder="" accept="image/png, image/jpg, image/jpeg, application/pdf">
                            <label class="input-file-label" for="file">Выбрать файл</label>
                        </div>
                        <div class="input-container">
                            <textarea name="additional" id="additional" cols="30" rows="10" placeholder=""></textarea>
                            <label for="additional">Дополнительное поле для ваших вопросов</label>
                        </div>
                        <button type="submit">Отправить</button>
                </form>
            </div>
        </div>
    </main>
</template>