<template>
    <v-container>
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <div class="header">
            <h1>{{ pathway.name }}</h1>
            <span class="bookmark-holder">

                <v-tooltip bottom >
                    <template v-slot:activator="{on, attrs}">
                        <v-icon class="unselected" v-bind="attrs" v-on="on" large >mdi-bookmark-outline</v-icon>
                    </template>
                    <span>Remove pathway from "My Pathways"</span>
                </v-tooltip>

                <v-tooltip bottom>
                    <template v-slot:activator="{on, attrs}">
                        <v-icon class="selected" v-bind="attrs" v-on="on" large >mdi-bookmark</v-icon>
                    </template>
                    <span>Add pathway to "My Pathways"</span>
                </v-tooltip>
            </span>
        </div>
        
        <p>{{ pathway.description }}</p>
        
        <div class="fab-container">
            <v-btn
                color="light grey" elevation="2" fab
                aria-label="Switch to nex tab on class selection"
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
                    :courses="courses[index]"
                    :pathway-id="pathwayID"
                    @checkbox-clicked="onCheckboxClicked()"
                />
            </v-tab-item>
        </v-tabs-items>
    </v-container>
</template>

<script>
import { pathwayCategories, pathways, courses } from '../../data/data.js'
import { modifierOrder } from '../../data/course-modifiers.js'
import CourseTable from '../../components/CourseTable'
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

/**
 * Converts array of class ids, ie ['art_history', ...]
 * into array of class objects
 * @param {array{string}} courseIds
 * @return {array{object}} courses
 */
function getCourses(courseIds) {
    let r = courseIds
        .map(course => courses[course])
        .filter(c => c.offered.fall || c.offered.spring || c.offered.summer);
    
    // Set the modifiers property (array of modifiers)
    r.forEach(c => c.modifiers = modifierOrder.filter(p => c.offered[p] || c.properties[p]))
    return r;
}

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
        // Array of all pathway courses, grouped
        priorities() {
            let pathway = this.pathway;
            return [pathway.priority1, pathway.priority2, pathway.priority3, pathway.priority4];
        },
        // Get array of all courses, grouped
        courses() {
            return this.priorities.map(getCourses);
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
                '3rd Course',
                'Minor (optional)'
            ].filter((_, index) => this.priorities[index] && this.priorities[index].length);
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

.header h1{
    display: inline-block;
}
.bookmark-holder {
    display: inline-flex;
    top: 0;
    cursor: pointer;
    z-index: 9;
}
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
