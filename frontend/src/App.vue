<template>
    <v-app id="app">
        <Header />

        <v-main class="main-content">
            <router-view />
        </v-main>

        <Footer id="footer" />
    </v-app>
</template>

<script>

import Header from './components/Header';
import Footer from './components/Footer';

import { DARK_MODE, DEFAULT_DARK_MODE } from './data/vuex.js'

export default {
    name: 'App',
    components: {
        Header,
        Footer
    },
    data: () => ({
        deleteClicked: false,
        searchInput: '',
        extension: ''
    }),
    mounted() {
        // Load dark mode directly from localStorage for faster response time
        // Note: localStorage saves as a string
        let darkMode = localStorage.getItem(DARK_MODE);
        this.$vuetify.theme.dark = darkMode === null ? DEFAULT_DARK_MODE : darkMode === 'true';
    },
    methods: {
        handleInput() {
            this.$root.$emit('changedFilter', this.searchInput)
        },
        clearProgress() {
            this.$root.$emit('resetProgress')
            this.$store.editingCourses = false
            location.reload()
        },
    },
}
</script>

<style lang="scss">
@import '@/styles/_globals.scss';
</style>

<style>
#app {
    font-family: 'Muli', sans-serif;
    overflow-x: hidden;
    overflow-y: hidden;
}

#footer {
    position: fixed;
    bottom: 0;
    width: 100%;
}

.main-content {
    min-height: 100vh;
}
</style>
