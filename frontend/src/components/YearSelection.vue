<template>
    <div>
        <div class="yeardropdown">
            <v-select
                v-model="selection"
                no-data-text
                :items="allyears"
                @input="updateYear()"
            />
        </div>
        <div style="clear: both;" />
    </div>
</template>

<script>
import { years } from '../data/data.js'

export default {
    name: 'YearSelection',
    data() {
        return {
            selection: this.$store.state.year
        }
    },
    computed: {
        allyears() {
            return years;
        }
    },
    created() {
        let choice = this.$store.state.year;
        if (choice === "") {
            this.$store.commit('changeYear', years[0]);
        }
        this.selection = this.$store.state.year;
    },
    methods: {
        updateYear() {
            this.$store.commit('changeYear', this.selection);
            if(this.$route.path !== "/pathways")  this.$router.push("/pathways");
            else location.reload();

        }
    }
}
</script>


<style>
.yeardropdown {
    max-width: 200px;
    float: right;
}
</style>
