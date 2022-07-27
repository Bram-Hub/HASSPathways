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
//import { pathways } from '../data/data.js'

export default {
    name: 'YearSelection',
    data() {
        return {
            selection: this.$store.state.year
        }
    },
    computed: {
        // allyears() {
        //     return pathways.keys()
        // }
        allyears() {
            return ["2021-2022","2020-2021","2019-2020","2018-2019","2017-2018"]
        }
    },
    methods: {
        updateYear() {
            this.$store.commit('changeYear',this.selection)
        }
    }
}
</script>

<style>
.yeardropdown {
    padding-top: 20px;
    padding-right: 10px;
    max-width: 200px;
    float: right;
}
</style>
