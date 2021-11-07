<template>
    <v-app id="app">
        <Header />

        <v-content class="main-content">
            <router-view />
        </v-content>

        <Footer />
    </v-app>
</template>

<script>

import Header from './components/Header';
import Footer from './components/Footer';

export default {
    name: 'App',
    components: {
        Header,
        Footer
    },
    data: () => ({
        deleteClicked: false,
        searchInput: '',
        extension: '',
    }),
    watch: {
        extension(newExtension) {
            localStorage.setItem('extension', newExtension)
        },
    },
    mounted() {
        console.log(this.$vuetify.breakpoint)
        if (localStorage.getItem('extension') == 'true') {
            this.extension = true
        }
 
        // Note: dark mode is saved as a string!
        this.$vuetify.theme.dark = localStorage.getItem('hass-pathways-dark-mode', 'true') === 'true';
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


.main-content {
    min-height: 100vh;
}

#button {
  float: right;
}

#topRightButtons .v-btn::before {
  background-color: transparent;
}

#header {
  height: 70px;
  background-color: #fa8072;
  color: white;
  font-family: 'Muli', sans-serif;
  font-size: 20px;
}

.v-btn--active .v-btn__content {
  color: black;
}

#title {
  color: white;
  text-decoration: none;
}

#app {
  font-family: 'Muli', sans-serif;
}

#list {
  height: 200px;
}

.combo-box {
    z-index: 200;
}
</style>
