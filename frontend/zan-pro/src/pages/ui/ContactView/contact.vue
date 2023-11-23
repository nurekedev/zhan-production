<script></script>

<template>
    <main class="contact">
        <section>
            <div>Контакты</div>
        </section>
        <article class="main-article">
            <div class="main-text">
                <p>Если у вас есть вопросы, Вы можете связаться с нами удобным для Вас способом</p>
            </div>
            <div class="form-group">
                <form action="" method="post">
                    <p>Получите бесплатную косультацию</p>
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
                    <div class="input-container">
                        <textarea name="additional" id="additional" cols="30" rows="10" placeholder=""></textarea>
                        <label for="additional">Дополнительное поле для ваших вопросов</label>
                    </div>
                    <button type="submit">Отправить</button>
                </form>
            </div>
        </article>
    </main>
</template>