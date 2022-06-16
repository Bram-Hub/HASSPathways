<template>
    <v-container>
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <h1>{{ pathway.name }}</h1>
        <p>{{ pathway.description }}</p>
        <div class="fab-container">
            <v-btn
                color="light grey" elevation="2" fab
                aria-label="Switch to next tab on class selection"
                @click="changeTabOnSelection = !changeTabOnSelection;"
            >
                <v-icon>
                    {{ changeTabOnSelection ? 'mdi-rotate-right-variant' : 'mdi-checkbox-blank-circle-outline' }}
                </v-icon>
            </v-btn>

            <v-btn
                color="red" elevation="2" fab
                aria-label="Clear courses"
                @click="deselectCourses()"
            >
                <v-icon>mdi-delete</v-icon>
            </v-btn>
        </div>

        <v-divider class="my-4" />

        <v-tabs
            v-model="tab"
            background-color="transparent"
            color="basil"
            grow
            center-active
        >
            <v-tabs-slider color="primary" />
            <v-tab
                v-for="item in classTabs"
                :key="item"
            >
                <small>{{ item }}</small>
            </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab" touchless>    
            <v-tab-item 
                v-for="(item, index) in classTabs"
                :key="item"
                :eager="true"
            >
                <CourseTable
                    :ref="index"
                    :courses="courses[item]"
                    :pathway-id="pathwayID"
                    @checkbox-clicked="onCheckboxClicked()"
                />
            </v-tab-item>
        </v-tabs-items>
    </v-container>
</template>

<script>
import { pathwayCategories, pathways, courses } from '../../data/data.js'
import CourseTable from '../../components/CourseTable'
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

export default {
    components: {
        CourseTable, Breadcrumbs
    },
    data() {
        return {
            tab: 0,
            category: '',
            changeTabOnSelection: false
        }
    },
    computed: {
        // Get id of the pathway, ie 'chinese_language'
        pathwayID() {
            // Should always be valid, see router/index.js
            let pathwayID = this.$route.query.pathway;
            return pathwayID;
        },
        // Get actual pathway object
        pathway() {
            return pathways[this.pathwayID];
        },
        // Name of category to display, ie 'Major Restricted'
        categoryName() {
            for (let category of pathwayCategories)
                if (category.pathways.includes(this.pathwayID))
                    return category.name;
            return '';
        },
        // Outputs an object containing the
        // different priorities for the pathway
        priorities() {
            let pathway = this.pathway;
            let out = {};
            out["Required"] = pathway.required ? pathway.required : null;
            out["One Of"] = pathway.one_of ? pathway.one_of : null;
            out["Remaining"] = pathway.remaining ? pathway.remaining : null;
            return out;
        },
        // Converts the courses into an actual array of objects for
        // priorities while they contain actual course objects
        courses() {
            let curr = this.priorities;

            // Search through all prios
            for(const prio in curr) {
                // Search through each course in the pathway
                for(const course_name in curr[prio]) {
                    const course = courses[course_name];
                    curr[prio][course_name] = course ? course : null;
                }
            }
            return curr;
        },
        // Get breadcrumb data
        breadcrumbs() {
            return breadcrumbs.pathway_template.map(x => x || {
                text: this.categoryName ?
                    `${this.pathway.name} (${this.categoryName})` :
                    this.pathway.name,
                href: '/pathway?pathway=' + encodeURIComponent(this.pathwayID)
            });
        },
        classTabs() {
            // Enable only non-empty tabs
            return [
                'Required',
                'One Of',
                'Remaining'
            ].filter((_, index) => Object.values(this.priorities)[index]);
        }
    },
    methods : {
        onCheckboxClicked(){
            if(this.changeTabOnSelection)
                this.tab += 1;
        },
        deselectCourses() {
            let tab = this.tab;
            this.courses[tab].forEach(course => {
                const c = { pathwayID: this.pathwayID, course: course.key };
                // delete course
                this.$store.commit('delCourse', c);
            })
            // deselect course
            // console.log(this.$refs.test)
            this.$refs[tab][0].deselectAll();
        }
    }
}
</script>

<style scoped>
.fab-container {
    position: fixed;
    right: 10px;
    bottom: 10px;
    width: 56px;
    height: 120px;
    z-index: 999;
    
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

@media only screen and (min-width: 600px) {
    .fab-container {
        right: 50px;
        bottom: 50px;
    }
}
</style>
