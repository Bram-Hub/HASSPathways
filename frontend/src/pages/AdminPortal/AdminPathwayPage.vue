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
                @change="filterCourses()"
            />
            <v-btn @click="submit()">
                Submit
            </v-btn>

            <v-data-table
                :headers="headers"
                :items="filteredCourses"
            > 
                <template slot="no-data">
                    No classes found, make sure to select a pathway in the dropdown above
                </template>

                <template #item.name="{ item }">
                    <v-text-field
                        v-model="item.name"
                        single-line
                        clearable   
                    />
                </template>

                <template #item.prefix="{ item }">
                    <v-text-field
                        v-model="item.prefix"
                        single-line
                        clearable   
                    />
                </template>

                <template #item.ID="{ item }">
                    <v-text-field
                        v-model="item.ID"
                        single-line
                        clearable   
                    />
                </template>
                <template #item.fall="{ item }">
                    <v-checkbox
                        v-model="item.offered.fall"
                        :ripple="false"
                    />
                </template> 
                <template #item.summer="{ item }">
                    <v-checkbox
                        v-model="item.offered.summer"
                        :ripple="false"
                    />
                </template> 
                <template #item.spring="{ item }">
                    <v-checkbox
                        v-model="item.offered.spring"
                        :ripple="false"
                    />
                </template> 
                <template #item.CI="{ item }">
                    <v-checkbox
                        v-model="item.properties.CI"
                        :ripple="false"
                    />
                </template> 
                <template #item.HI="{ item }">
                    <v-checkbox
                        v-model="item.properties.HI"
                        :ripple="false"
                    />
                </template> 
                <template #item.delete="{ item }">
                    <v-btn color="error" @click="remove(item.name)">
                        <v-icon>mdi-delete</v-icon>
                    </v-btn>
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
                { text: 'Prefix', value: 'prefix' },
                { text: 'Course Code', value: 'ID' },
                { text: 'Fall', value: 'fall' },
                { text: 'Spring', value: 'spring' },
                { text: 'Summer', value: 'summer' },
                { text: 'Comm Intensive', value: 'CI' },
                { text: 'Hass Inquiry', value: 'HI' },
                { text: 'Delete From Pathway', value: 'delete' },
            ],
            filteredCourses: []
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
        },
        filterCourses() {
            if(this.selectedPathway == null || this.selectedPathway == "") {
                return [];
            }
            let pathwayID = this.selectedPathway.toLowerCase().replace(/ /g, '_').replace(/,/g, '');
            let pathway = pathways[pathwayID];
            if(pathway != null) {
                let classes = new Set();
                for(const prio in pathway) {
                    if(prio.substring(0, 8) == "priority") {
                        for(const course in pathway[prio]) {
                            let clazz = courses[pathway[prio][course]];
                            clazz = JSON.parse(JSON.stringify(clazz));
                            classes.add(clazz);
                        }
                    }
                }
                this.filteredCourses = Array.from(classes);
            }
            else {
                this.filteredCourses = [];
            }
        },
        submit() {
            const classes = this.filteredCourses;

            for(const clazz in classes) {
                const key = classes[clazz].name.toLowerCase().replace(/ /g, '_').replace(/,/g, '').replace(/-/g, '_');
                const curr = JSON.parse(JSON.stringify(classes[clazz]));
                const course = courses[key];
                if(JSON.stringify(curr) != JSON.stringify(course)) {
                    console.log(curr);
                }
            }
        },
        remove(name) {
            name = name.toLowerCase().replace(/ /g, '_').replace(/,/g, '').replace(/-/g, '_');
            console.log("remove " + name + " from " + this.selectedPathway);
        }
    }
}
</script>

<style>
    
</style>