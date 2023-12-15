<script>
    import { computed } from 'vue';
    import { onMounted } from 'vue';
    import { useStore } from 'vuex';

    export default {
        name: 'Footer',
        setup() {
            // State
            const store = useStore();

            // Computed
            const fbUrl = computed(() => store.getters.getFb);
            const vkUrl = computed(() => store.getters.getVk);
            const igUrl = computed(() => store.getters.getIg);
            const xUrl = computed(() => store.getters.getX);

            // Methods

            // Life cycle
            onMounted(async () => {
                await store.dispatch('getFbUrl');
                await store.dispatch('getVkUrl');
                await store.dispatch('getIgUrl');
                await store.dispatch('getXUrl');
            });
            return {
                fbUrl,
                vkUrl,
                igUrl,
                xUrl,
            };
        },
    };
</script>

<template>
    <footer>
        <div class="f-cont">
            <div>
                <img src="../../model/logo.svg" alt="svg logo" />
                <div>
                    <p>{{ $t('navWork') }}</p>
                    <p>© 2023. All rights reserved</p>
                </div>
            </div>
            <div>
                <p>{{ $t('footerContact') }}</p>
                <p>
                    {{ $t('footerMail') }}:
                    <a href="#">KasiaBasiaTosia@gmail.com</a>
                </p>
                <p>{{ $t('footerNumber') }}:</p>
            </div>
            <div>
                <p>{{ $t('footerSocial') }}</p>
                <div>
                    <a :href="fbUrl" target="_blank"
                        ><img src="../../model/facebook.svg"
                    /></a>
                    <a :href="xUrl" target="_blank"
                        ><img src="../../model/twiter.svg"
                    /></a>
                    <a :href="igUrl" target="_blank"
                        ><img src="../../model/instagram.svg"
                    /></a>
                </div>
            </div>
        </div>
    </footer>
</template>
