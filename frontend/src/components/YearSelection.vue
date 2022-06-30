<template>
    <div style="max-width: 500px; float: right;">
        <v-select :items="allyears" :label="year" />
    </div>
</template>

<script>
import { pathways } from '../data/data.js'

export default {
    name: 'YearSelection',
    data() {
        return {
            year: "2021-2022"
        }
    },
    computed: {
        // allyears() {
        //     return pathways.keys()
        // }
        allyears() {
            return ["2021-2022","2020-2021","2019-2020","2018-2019","2017-2018"]
        }
    }
}
</script>


<style>

</style>
