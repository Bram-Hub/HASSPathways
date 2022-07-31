<template>
    <v-app-bar app flat dense class="navbar">
        <router-link to="/">
            <v-img
                class="pl-6 pr-8 ml-4"
                height="60"
                width="60"
                :src="this.$vuetify.theme.dark ? require('../assets/dark-mode-logo.png') : require('../assets/light-mode-logo.png')"
            />
        </router-link>
        <v-container fluid>
            <v-layout row align-center justify-end>
                <YearSelection />
                <DarkLightModeButton />
                <HeaderNav />
            </v-layout>
        </v-container>
    </v-app-bar>
</template>       

<script>
import DarkLightModeButton from './DarkLightModeButton.vue'
import HeaderNav from './HeaderNav.vue'
import YearSelection from '../components/YearSelection.vue'

export default {
    name: 'Header',
    components: { DarkLightModeButton, 
    HeaderNav,
    YearSelection }
}
</script>

<style scoped>
.navbar {
    border-bottom: 3px solid var(--v-primary-base) !important;
}

/* Remove navbar padding */
/deep/ .v-toolbar__content {
    padding: 0px !important;
}
</style>
