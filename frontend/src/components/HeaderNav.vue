<template>
    <div>
        <v-btn
            class="button"
            elevation="0"
            depressed
            tile
            :to="{ name: 'activity' }"
        >
            <v-icon class="icon">
                mdi-bookmark-box-multiple
            </v-icon>
            <span class="text">My Pathways</span>
        </v-btn>
        <v-btn
            class="button"
            elevation="0"
            depressed
            tile
            :to="{ name: 'home' }"
            @click="clearProgress()"
        >
            <v-icon class="icon">
                mdi-plus
            </v-icon>
            <span class="text">Add Pathway</span>
        </v-btn>
    </div>
</template>

<script>
export default {
    name: 'HeaderNav'
}
</script>

<style scoped>
/* Override button active color, otherwise
 * it defaults to black 
 * Note: the >>> is NOT a typo */
>>> .v-btn--active .v-btn__content {
    color: inherit;
}

.text {
    font-size: 0.85em;
    display: none;
}

@media only screen and (max-width: 600px) {
    .button {
        padding: 0 !important;
        min-width: 48px !important;
    }
}

@media only screen and (min-width: 600px) {
    .icon { margin-right: 8px; }
    .text { display: block; }
}
</style>