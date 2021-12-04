<template>
    <v-container>
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        
        <h1>{{ pathway.name }}</h1>
        <p>{{ pathway.description }}</p>

        <div class="fab-container">
            <v-btn
                color="green" elevation="2" fab
                aria-label="Save pathway"
            >
                <v-icon>mdi-content-save</v-icon>
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
                <ClassTable :classes="classes[index]" :pathway-id="pathwayID" />
            </v-tab-item>
        </v-tabs-items>
    </v-container>
</template>

<script>
import { mapMutations } from 'vuex'
import { pathwayCategories, pathways, courses } from '../../data/data.js'
import { modifierOrder } from '../../data/course-modifiers.js'
import getColorFromCategry from '../../helpers/category-colors.js'

import ClassTable from '../../components/ClassTable'
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

/**
 * Converts array of class ids, ie ['art_history', ...]
 * into array of class objects
 * @param {array{string}} classIds
 * @return {array{object}} classes
 */
function getClasses(classIds) {
    let r = classIds
        .map(clazz => courses[clazz])
        .filter(c => c.offered.fall || c.offered.spring || c.offered.summer);
    
    // Set the modifiers property (array of modifiers)
    r.forEach(c => c.modifiers = modifierOrder.filter(p => c.offered[p] || c.properties[p]))
    return r;
}

export default {
    components: {
        ClassTable, Breadcrumbs
    },
    data() {
        return {
            tab: null,
            category: ''
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
        // Array of all pathway classes, grouped
        priorities() {
            let pathway = this.pathway;
            return [pathway.priority1, pathway.priority2, pathway.priority3, pathway.priority4];
        },
        // Get array of all classes, grouped
        classes() {
            return this.priorities.map(getClasses);
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
            // Note: assumes empty tabs will always occur at end
            // with no spaces between
            return [
                '1st Course',
                '2nd Course',
                '4000 Level',
                'Minor (optional)'
            ].filter((_, index) => this.priorities[index] && this.priorities[index].length);
        }
    },
    mounted() {
        // Adjust color scheme based on pathway category
        let color = getColorFromCategry(this.categoryName);
        this.$vuetify.theme.themes.light.primary = color;
        this.$vuetify.theme.themes.dark.primary = color;
    },
    methods: {
        ...mapMutations([
            'setSelectedCourse1',
            'setSelectedCourse2',
            'setSelectedCourse3',
            'setSelectedPathway',
        ]),
        findAllCourses(path) {
            var courses = []
            for (var x = 0; x < path.priority1.length; x++) {
                courses.push(this.findCourse(path.priority1[x]))
            }
            return courses
        },
        selectCourse(course, path) {
            this.setSelectedPathway(path.name)
            this.setSelectedCourse1(course)
            if (this.$store.editingCourses) {
                this.setSelectedCourse2(null)
                this.setSelectedCourse3(null)
            }
            console.log(course)
            this.$emit('nextBucket', this.nextBucketNumber)
            this.$root.$emit('makeSecondCourseEditable', true)
            this.$root.$emit('changeCurrent', 2)
            this.$root.$emit(`closePanels`)
        },
        findCourse(course) {
            var courses = this.allCourses
            for (var courseKey in courses) {
                if (course == courses[courseKey].pk) {
                    return courses[courseKey]
                }
            }
        },
    },
}
</script>

<style scoped>
.fab-container {
    position: fixed;
    right: 10px;
    bottom: 10px;
    width: 56px;
    height: 56px;
    z-index: 999;
    
    display: flex;
    justify-content: space-between;
}

@media only screen and (min-width: 600px) {
    .fab-container {
        right: 50px;
        bottom: 50px;
    }
}
</style>
