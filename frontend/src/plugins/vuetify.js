import Vue from 'vue'
import Vuetify, { colors } from 'vuetify/lib'

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: '#ff4040', // main color NOT background
                secondary: '#b0bec5', // accent color, unused as of now
                anchor: '#1976d2', // link color
            },
            dark: {
                primary: '#ff4040',
                secondary: '#b0bec5',
                anchor: '#75baff',
            },
        },
        options: {
            customProperties: true
        }
    },
})
