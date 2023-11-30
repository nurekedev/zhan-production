<script>
    export default {
        name: 'ToastNotification',
        props: {message: ''},
        data() {
            return {
                visible: false,
            }
        },
        methods: {
            showToast() {
                this.visible = true;
                setTimeout(() => {
                    this.visible = false
                }, 3000);
            }
        }
    }
</script>

<template>
    <div class="toast-container" v-if="visible">
        <div class="toast">{{ message }}</div>
    </div>
</template>