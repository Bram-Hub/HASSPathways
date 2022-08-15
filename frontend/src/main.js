import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import Toast from 'vue-toastification'
import store from './store/store.js'

import 'vue-toastification/dist/index.css'

Vue.use(Toast, {
    transition: 'Vue-Toastification__bounce',
    maxToasts: 1,
    newestOnTop: true,
})

Vue.config.productionTip = false;

new Vue({
    router,
    vuetify,
    store,
    initializeStore() {
        store.commit('initializeStore')
    },
    render: (h) => h(App),
}).$mount('#app');
