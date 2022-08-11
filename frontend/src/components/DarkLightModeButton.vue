<template>
    <v-tooltip bottom>
        <template #activator="{off}">
            <v-switch
                v-model="isLight"
                inset small fab
                elevation="0"
                size="small"
                color="yellow darken-2"
                :prepend-icon="correctIcon"
                style="padding-top:21px;"
                v-on="off"
                @click="darkMode"
            />
        </template>
        <span>Switch to Light Mode</span>
    </v-tooltip>
</template>


<script>
export default {
    name: 'DarkLightModeButton',
    data() {
        return {
            isLight: !this.$store.state.darkMode
        }
    },
    computed: {
        correctIcon() {
            return this.isLight ? "mdi-white-balance-sunny" : "mdi-moon-waxing-crescent"
        }
    },
    methods: {
        darkMode() {
            //prepend-icon="mdi-moon-waxing-crescent"
            this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
            this.$store.commit('setDarkMode', !this.isLight);
        }

    }
}
</script>

<style scoped>
/* Fix button highlighting getting stuck */
.button::before {
    opacity: 0 !important;
}

.button {
    opacity: 0.7;
}

.button:hover {
    opacity: 1;
}
</style>
