<template>
    <v-app-bar
        app
        flat
        dense
        class="navbar"
    >
        <router-link to="">
            <v-img
                class="pl-6 pr-8 ml-4"
                height="60"
                width="40"
                :src="require('../assets/logo.png')"
                @click="clearProgress()"
            />
        </router-link>

        <v-container fluid>
            <v-layout row align-content-center justify-end class="">
                <v-btn
                    id="button"
                    class="hidden-sm-and-down text-capitalize"
                    rounded
                    elevation="4"
                    depressed
                    active-class="v-btn--active toolbar-btn-active blue-grey lighten-3"
                    :to="{ name: 'activity' }"
                >
                    My Pathways
                </v-btn>
                <v-btn
                    id="button"
                    class="hidden-sm-and-down mr-2 text-capitalize"
                    active-class="v-btn--active toolbar-btn-active blue-grey lighten-3"
                    rounded
                    elevation="4"
                    depressed
                    :to="{ name: 'home' }"
                    @click="clearProgress()"
                >
                    Add Pathways
                </v-btn>
            </v-layout>

            <div>
                <v-tooltip v-if="!$vuetify.theme.dark" bottom>
                    <template #activator="{ on }">
                        <v-btn
                            color="info" small fab v-on="on"
                            @click="darkMode"
                        >
                            <v-icon class="mr-1">
                                mdi-moon-waxing-crescent
                            </v-icon>
                        </v-btn>
                    </template>
                    <span>Dark Mode On</span>
                </v-tooltip>

                <v-tooltip v-else bottom>
                    <template #activator="{ on }">
                        <v-btn
                            color="info" small fab v-on="on"
                            @click="darkMode"
                        >
                            <v-icon color="yellow">
                                mdi-white-balance-sunny
                            </v-icon>
                        </v-btn>
                    </template>
                    <span>Dark Mode Off</span>
                </v-tooltip>
            </div>
        </v-container>
    </v-app-bar>
</template>

<script>
export default {
    name: 'Header',
    data() {
        return {

        }
    },
    methods: {
        darkMode() {
            this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
            localStorage.setItem('hass-pathways-dark-mode', this.$vuetify.theme.dark);
        }
    }
}
</script>

<style scoped>
.navbar {
    border-bottom: 3px solid var(--v-primary-base) !important;
}
</style>
