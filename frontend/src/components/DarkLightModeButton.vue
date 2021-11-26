<template>
    <v-tooltip v-if="!$vuetify.theme.dark" bottom>
        <template #activator="{on}">
            <v-btn
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
            localStorage.setItem('hass-pathways-dark-mode', this.$vuetify.theme.dark);
        }
    }
}
</script>
