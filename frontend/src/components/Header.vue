<template>
    <v-app-bar
        app
        fixed
        flat
        dense
        color="#c65353"
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
                <v-text-field
                    solo label="Search" dense hide-details
                    prepend-inner-icon="search" light color="blue"
                    flat style="max-width: 400px"
                />

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
        </v-container>
    </v-app-bar>
</template>

<script>
export default {
    name: 'Header',
    data() {
        return {

        }
    }
}
</script>

<style scoped>

</style>
