<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <v-autocomplete
                v-model="selectedPathway"
                clearable
                rounded
                solo
                :items="pathways"
                label="Pathways"
            />
            <v-data-table
                :headers="headers"
                :items="filteredCourses"
            >
                <template slot="no-data">
                    No classes found, make sure to select a pathway in the dropdown above
                </template>

                <template #item.name="{ item }">
                    <a :href="toClass(item.name)" class="text-decoration-none">
                        {{ item.name }}
                    </a>
                </template> 
                <template #item.fall="{ item }">
                    <v-simple-checkbox
                        color="primary"
                        v-model="item.offered.fall"
                        readonly
                    />
                </template> 
                <template #item.summer="{ item }">
                    <v-simple-checkbox
                        color="primary"
                        v-model="item.offered.summer"
                        readonly
                    />
                </template> 
                <template #item.spring="{ item }">
                    <v-simple-checkbox
                        color="primary"
                        v-model="item.offered.spring"
                        readonly
                    />
                </template> 
                <template #item.CI="{ item }">
                    <v-simple-checkbox
                        color="primary"
                        v-model="item.properties.CI"
                        readonly
                    />
                </template>
            </v-data-table>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'
import { courses, pathways } from '../../data/data.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.admin_pathway_page,
            selectedPathway: "",
            pathways: [],
            headers: [
                {
                    text: 'Course Name',
                    align: 'start',
                    value: 'name',
                },
                { text: 'Fall', value: 'fall' },
                { text: 'Spring', value: 'spring' },
                { text: 'Summer', value: 'summer' },
                { text: 'Deptartment', value: 'prefix' },
                { text: 'ID', value: 'ID' },
                { text: 'CI', value: 'CI' },
            ],
        }
    },
    computed: {
        filteredCourses() {
            if(this.selectedPathway == null || this.selectedPathway == "") {
                return [];
            }
            let pathwayID = this.selectedPathway.toLowerCase().replace(/ /g, '_').replace(/,/g, '');
            let pathway = pathways[pathwayID];

            let classes = new Set();
            for(const prio in pathway) {
                if(prio.substring(0, 8) == "priority") {
                    for(const course in pathway[prio]) {
                        let clazz = courses[pathway[prio][course]];
                        for(let prop in clazz.properties) {
                            if(clazz.properties[prop] == 0) {
                                clazz.properties[prop] = false;
                            } 
                            else {
                                clazz.properties[prop] = true;
                            } 
                        }
                        for(let offer in clazz.offered) {
                            if(clazz.offered[offer] == 0) {
                                clazz.offered[offer] = false;
                            } 
                            else {
                                clazz.offered[offer] = true;
                            } 
                        }
                        classes.add(clazz);
                    }
                }
            }
            return Array.from(classes);
        }
    },
    created() {
        this.pathways = [];
        for(const key in pathways) {
            this.pathways.push(pathways[key].name);
        }
    },
    methods: {
        toClass(clazz) {
            let urlStart = "/admin-portal/course?class=";
            let urlEnd = clazz.toLowerCase().replace(/ /g, '_').replace(/,/g, '');
            const finalURL = urlStart + urlEnd;
            return finalURL;
        }
    }
}
</script>

<style>
    
</style>