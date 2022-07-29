<template>
    <v-switch
        
        :value="$vuetify.theme.dark"
        small fab elevation="0"
        inset
        v-on="off"
        v-model="t"
        :prepend-icon="correctIcon"
                
        color="yellow darken-2"
            
        size="small"
        @change="darkMode"
        style="padding-top:21px;"
    >
    </v-switch>

</template>


<script>
export default {
    name: 'DarkLightModeButton',
    //:defaultState="true"
    props: {
        defaultState: {
            type: Boolean, 
            default: false
        }
    },
    computed:{
        correctIcon(){
            if(this.$vuetify.theme.dark){
               return "mdi-moon-waxing-crescent";
            }
            else{
                return "mdi-white-balance-sunny";
            }
        }
    },
    methods: {
        darkMode() {
            //prepend-icon="mdi-moon-waxing-crescent"
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
    opacity: 0.7;
}

.button:hover {
    opacity: 1;
}
</style>
