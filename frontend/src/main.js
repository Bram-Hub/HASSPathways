import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import Vuex from 'vuex'
import Toast from 'vue-toastification'
import createPersistedState from 'vuex-persistedstate'


import 'vue-toastification/dist/index.css'

Vue.use(Toast, {
    transition: 'Vue-Toastification__bounce',
    maxToasts: 1,
    newestOnTop: true,
})

Vue.use(Vuex);

// Keys defined in /data in vuex.js
import { DARK_MODE, PATHWAYS, DEFAULT_DARK_MODE } from './data/vuex.js'

const store = new Vuex.Store({
    state: {
        darkMode: true,

        // { pathway_id: { courses: [course_ids, ...] } }
        // Additional keys may be added as necessary for each pathway
        pathways: {},
    },
    plugins: [createPersistedState()],
    mutations: {
        initializeStore(state) {
            let darkMode = localStorage.getItem(DARK_MODE);
            state.darkMode = darkMode === null ? DEFAULT_DARK_MODE : darkMode === 'true';
            state.pathways = localStorage.getItem(PATHWAYS) || {};
        },
        setDarkMode(state, val=true) {
            state.darkMode = val;
            localStorage.setItem(DARK_MODE, val);
        },
        updateCourses(state, pathwayID, newCourses) {
            if (!state.pathways[pathwayID])
                state.pathways[pathwayID] = {};
            state.pathways[pathwayID].courses = newCourses;
            localStorage.setItem(PATHWAYS, state.pathways);
        }
    },
    getters: {}
});

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
