<template>
    <v-tooltip v-if="!$vuetify.theme.dark" bottom>
        <template #activator="{on}">
            <v-btn
                class="mr-2 button"
                small fab tile elevation="0"
                v-on="on"
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
        <template #activator="{on}">
            <v-btn
                class="mr-2 button"
                small fab tile elevation="0"
                v-on="on"
                @click="darkMode"
            >
                <v-icon color="yellow">
                    mdi-white-balance-sunny
                </v-icon>
            </v-btn>
        </template>
        <span>Dark Mode Off</span>
    </v-tooltip>
</template>

<script>
export default {
    name: 'DarkLightModeButton',

    methods: {
        darkMode() {
            this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
            this.$store.commit('setDarkMode', this.$vuetify.theme.dark);
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
    opacity: 0.8;
}

.button:hover {
    opacity: 1;
}
</style>
