<template>
  <div style="background:blue;">
    <loading :active.sync="visible" :can-cancel="true"></loading>
    <button @click.prevent="show()">Show</button>
  </div>
</template>

<script>
  Vue.use(VueLoading);

let app = new Vue({
    el: '#app',
    data() {
        return {
            visible: false
        }
    },
    components: {
        Loading: VueLoading
    },
    methods: {
        open() {
            console.log('open was clicked, will auto hide');
            let loader = this.$loading.show({
                loader: 'dots'
            });
            setTimeout(() => loader.hide(), 3 * 1000)
        },
        show() {
            console.log('show was clicked, click to hide');
            // do AJAX here
            this.visible = true
        }
    }
});
</script>

