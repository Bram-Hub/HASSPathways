<template>
    <v-container>
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <div class="header">
            <h1>{{ pathway.name }}</h1>
            <span class="bookmark-holder">

                <v-tooltip bottom v-if="bookmarkSelected">
                    <template v-slot:activator="{on, attrs}">
                        <v-icon 
                            class="unselected" 
                            v-bind="attrs" 
                            v-on="on" 
                            large 
                            @click="selectBookmark()" 
                        >
                            mdi-bookmark-outline
                        </v-icon>
                    </template>
                    <span>Add pathway to "My Pathways"</span>
                </v-tooltip>

                <v-tooltip bottom v-else>
                    <template v-slot:activator="{on, attrs}">
                        <v-icon 
                            class="selected" 
                            v-bind="attrs" 
                            v-on="on" 
                            large 
                            @click="deselectBookmark()" 
                        >
                            mdi-bookmark
                        </v-icon>
                    </template>
                    <span>Remove pathway from "My Pathways"</span>
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
            changeTabOnSelection: false,
            bookmarkSelected: false,
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
        selectBookmark() {
            // this works
            console.log("bookmarking")
            this.bookmarkSelected = !this.bookmarkSelected;
            const c = { pathwayID: this.pathwayID, course: null };
            this.$store.commit('addCourse', c);
        },
        deselectBookmark() {
            console.log("un-bookmarking");
            this.bookmarkSelected = !this.bookmarkSelected;
            // add logic to store the state the bookmark now
            // check to see what courses are selected
            console.log(this.pathwayID)


            
            this.$store.commit('delPathway', this.pathwayID)
        },
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
            this.$refs[tab][0].deselectAll(); 
           /* <!-- ! this is sus -->
            * this WILL break with the current implementation of graph view
            *  because this.$refs[tab] gives me an array of all of the courseTable components
            *   on the DOM. Right now, there is only one, but with the current implementation
            *    of graph view, there will be more courseTable components which will make the
            *     array that this.$refs[tab] gives have multiple couresTable elements
            *      this should be revamped in the future to change how I deselect courses
            * 
            * <!-- --from graph view's branch-- -->
            * this.$refs[tab] is an array of all of the courseTable components
            *  right now there are two on each page, with this.$refs[tab][0] being the component
            *   on graph view, and $this.refs[tab][1] being the component on the regular view
            *    
            * this should be changed in the future
            */
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
