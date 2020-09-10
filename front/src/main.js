// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueMq from 'vue-mq'
import VueAxios from 'vue-axios'
import axios from 'axios'
import VueSweetalert2 from 'vue-sweetalert2';
import SweetModal from 'sweet-modal-vue/src/plugin.js'

Vue.config.productionTip = false


Vue.use(BootstrapVue);
Vue.use(VueSweetalert2);
Vue.use(SweetModal);

// /* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   router,
//   store,
//   components: { App },
//   template: '<App/>'
// })

new Vue({
  router,
  store,
  beforeCreate() {
    this.$store.dispatch("loginRefresh")
  },
  render: h => h(App),
}).$mount('#app');
