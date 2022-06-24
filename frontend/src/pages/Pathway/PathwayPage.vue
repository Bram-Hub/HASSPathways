<template>
    <v-container style="width:75%">
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <div class="header">
            <h1>{{ pathway.name }}</h1>

            <span class="bookmark-holder">
                <v-tooltip v-if="bookmarkSelected" bottom>
                    <template #activator="{on, attrs}">
                        <v-icon
                            class="selected"
                            v-bind="attrs"
                            large
                            v-on="on"
                            @click="deselectBookmark()"
                        >
                            mdi-bookmark
                        </v-icon>
                    </template>
                    <span>Remove pathway from "My Pathways"</span>
                </v-tooltip>
                <v-tooltip v-else bottom>
                    <template #activator="{on, attrs}">
                        <v-icon
                            class="unselected"
                            v-bind="attrs"
                            large
                            v-on="on"
                            @click="selectBookmark()"
                        >
                            mdi-bookmark-outline
                        </v-icon>
                    </template>
                    <span>Add pathway to "My Pathways"</span>
                </v-tooltip>
            </span>
        </div>
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
            <div v-if="item === 'Remaining'" id="info">
                <h4 v-if="fourthousand">At least one course must be at the 4000 level</h4>
            </div>
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
            changeTabOnSelection: false,
            bookmarkSelected: false,
        }
    },
    computed: {
        // Returns true if the pathway is already in the
        //  'My Pathways' page
        bookmarked() {
            return this.$store.getters.pathwayBookmarked(this.pathwayID);
        },
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
        },
        fourthousand() {
            return this.pathway.remaining_header.indexOf("4000") !== -1
        }
    },
    mounted() {
        this.bookmarkSelected = this.bookmarked;
    },
    methods : {
        test() {
            let output = Object.entries(this.$store.state.pathways).map(v => { return {
                name: v[0],
                courses: v[1].courses,
                bookmarked: v[1].bookmarked
            }});
            console.log(output)
            console.log(this.$store.getters.pathwayBookmarked(this.pathwayID))
        },
        selectBookmark() {
            this.bookmarkSelected = !this.bookmarkSelected;
            // const c = { pathwayID: this.pathwayID, course: "null" };
            // this.$store.commit('addCourse', c);
            this.$store.commit('bookmarkPathway', this.pathwayID);
        },
        deselectBookmark() {
            // <!--// idk how to use vuex to get which classes are already selected
            // <!--//  so im just going to go through each checkbox and see if
            // <!--//   it is toggled or not
            // nvm i figured it out

            this.$store.commit('unBookmarkPathway', this.pathwayID);
            this.bookmarkSelected = !this.bookmarkSelected;

        },
        onCheckboxClicked(){
            if(this.changeTabOnSelection)
                this.tab += 1;

        },
        deselectCourses() {
            let pathway = this.$store.state.pathways[this.pathwayID];
            pathway.courses.forEach(course => {
                const c = { pathwayID: this.pathwayID, course: course };
                // delete course
                this.$store.commit('delCourse', c);
            })
            // deselect course
            for(const i in this.classTabs) {
                this.$refs[i][0].deselectAll();
            }
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
#container {
    /* margin: 0; */
}
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
