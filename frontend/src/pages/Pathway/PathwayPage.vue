<template>
    <v-container>
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <!-- <v-btn @click="debug()">click me</v-btn> -->
        <div class="header">
            <h1>{{ pathway.name }}</h1>

            <span class="bookmark-holder">
                <v-tooltip v-if="bookmarkSelected" bottom>
                    <template #activator="{ on, attrs }">
                        <v-icon
                            class="selected"
                            v-bind="attrs"
                            large
                            v-on="on"
                            @click="deselectBookmark()"
                        >mdi-bookmark</v-icon>
                    </template>
                    <span>Remove pathway from "My Pathways"</span>
                </v-tooltip>
                <v-tooltip v-else bottom>
                    <template #activator="{ on, attrs }">
                        <v-icon
                            class="unselected"
                            v-bind="attrs"
                            large
                            v-on="on"
                            @click="selectBookmark()"
                        >mdi-bookmark-outline</v-icon>
                    </template>
                    <span>Add pathway to "My Pathways"</span>
                </v-tooltip>
            </span>
        </div>
        <p>{{ pathway.description }}</p>
        <v-btn @click="toggleGraph()">
            click me to toggle graph view
        </v-btn>
        <v-container v-show="showGraph">
        <v-btn @click="resize(1, 2)">1:2</v-btn>
        <v-btn @click="resize(1, 1)">1:1</v-btn> 
        <v-btn @click="resize(2, 1)">2:1</v-btn>
        <hr/>
            <div id="graphView">
                <div class="graph-fab-container">
                    <v-btn
                        color="grey"
                        elevation="2"
                        fab
                        aria-label="Show class description on hover"
                        @click="hover = !hover"
                    >
                        <v-icon>
                            {{
                                !hover
                                    ? 'mdi-comment-text-outline'
                                    : 'mdi-comment-text'
                            }}
                        </v-icon>
                    </v-btn>
                </div>
                <div id="graphTabs">
                    <div v-for="key in classTabs" :key="key" class="tab" ref="tab">
                        <h2 class="courseTitle">
                            {{ key }}
                        </h2>
                        <CourseTable
                            :ref="key"
                            :courses="courses[key]"
                            :pathway-id="pathwayID"
                            :desc="false"
                            :searchBar="false"
                            :graph="true"
                            :hover="hover"
                            :category="key"
                            @checkbox-clicked="onCheckboxClicked"
                        />
                    </div>
                </div>

            </div>
        </v-container>
        <v-container v-show="!showGraph">
            <div class="fab-container">
                <v-btn
                    color="light grey"
                    elevation="2"
                    fab
                    aria-label="Switch to nex tab on class selection"
                    @click="changeTabOnSelection = !changeTabOnSelection"
                >
                    <v-icon>
                        {{
                            changeTabOnSelection
                                ? 'mdi-rotate-right-variant'
                                : 'mdi-checkbox-blank-circle-outline'
                        }}
                    </v-icon>
                </v-btn>

                <v-btn
                    color="red"
                    elevation="2"
                    fab
                    aria-label="Clear courses"
                    @click="deselectCourses()"
                >
                    <v-icon>mdi-delete</v-icon>
                </v-btn>
            </div>

            <v-divider class="my-4" />

            <v-tabs v-model="tab" background-color="transparent" color="basil" grow>
                <v-tabs-slider color="primary" />
                <v-tab v-for="item in classTabs" :key="item">
                    <small>{{ item }}</small>
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab" touchless>
                <v-tab-item v-for="item in classTabs" :key="item" :eager="true">
                    <CourseTable
                        :ref="item"
                        :courses="courses[item]"
                        :pathway-id="pathwayID"
                        :show-desc="true"
                        :category="item"
                        @checkbox-clicked="onCheckboxClicked"
                    />
                </v-tab-item>
            </v-tabs-items>
        </v-container>
    </v-container>
</template>

<script>
import { pathwayCategories, pathways, courses } from '../../data/data.js'
import CourseTable from '../../components/CourseTable'
// import GraphTab from '../../components/GraphTab.vue'
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

export default {
    components: {
        CourseTable,
        Breadcrumbs,
    },
    data() {
        return {
            tab: null,
            category: '',
            showGraph: false,
            changeTabOnSelection: false,
            hover: false,
            bookmarkSelected: false,
        }
    },
    computed: {
        // Returns true if the pathway is already in the
        //  'My Pathways' page
        bookmarked() {
            return this.$store.getters.pathwayBookmarked(this.pathwayID)
        },
        // Get id of the pathway, ie 'chinese_language'
        pathwayID() {
            // Should always be valid, see router/index.js
            let pathwayID = this.$route.query.pathway
            return pathwayID
        },
        // Get actual pathway object
        pathway() {
            return pathways[this.pathwayID]
        },
        // Name of category to display, ie 'Major Restricted'
        categoryName() {
            for (let category of pathwayCategories)
                if (category.pathways.includes(this.pathwayID)) return category.name
            return ''
        },
        // Outputs an object containing the
        // different priorities for the pathway
        priorities() {
            let pathway = this.pathway
            let out = {}
            out['Required'] = pathway.required ? pathway.required : null
            out['One Of'] = pathway.one_of ? pathway.one_of : null
            out['Remaining'] = pathway.remaining ? pathway.remaining : null
            return out
        },
        // Converts the courses into an actual array of objects for
        // priorities while they contain actual course objects
        courses() {
            let curr = this.priorities

            // Search through all prios
            for (const prio in curr) {
                // Search through each course in the pathway
                for (const course_name in curr[prio]) {
                    const course = courses[course_name]
                    curr[prio][course_name] = course ? course : null
                }
            }
            return curr
        },
        // Get breadcrumb data
        breadcrumbs() {
            return breadcrumbs.pathway_template.map(
                (x) =>
                    x || {
                        text: this.categoryName
                            ? `${this.pathway.name} (${this.categoryName})`
                            : this.pathway.name,
                        href: '/pathway?pathway=' + encodeURIComponent(this.pathwayID),
                    }
            )
        },
        classTabs() {
            // Enable only non-empty tabs
            return ['Required', 'One Of', 'Remaining'].filter(
                (_, index) => Object.values(this.priorities)[index]
            )
        },
    },
    mounted() {
        this.bookmarkSelected = this.bookmarked
    },
    methods: {
        debug() {
            // console.log(this.hover)
            console.log('calculating how wide each section should be')
            let lengths = {}
            let lengthsArr = this.classTabs.map(
                (category) => Object.keys(this.courses[category]).length
            )
            this.classTabs.forEach((category) => {
                lengths[category] = Object.keys(this.courses[category]).length
            })
            for (let i = 0; i < lengthsArr.length; i++) {
                let key_i = Object.keys(lengths)[i]
                for (let j = 0; j < lengthsArr.length; j++) {
                    if (i == j) {
                        continue
                    }
                    let key_j = Object.keys(lengths)[j]
                    console.log(
                        `Ratio for ${key_i}:${key_j}: ${Math.floor(
                            lengthsArr[i] / lengthsArr[j]
                        )}`
                    )
                }
            }
            console.log(lengths)
        },
        selectBookmark() {
            this.bookmarkSelected = !this.bookmarkSelected
            this.$store.commit('bookmarkPathway', this.pathwayID)
        },
        deselectBookmark() {
            this.$store.commit('unBookmarkPathway', this.pathwayID)
            this.bookmarkSelected = !this.bookmarkSelected
        },
        onCheckboxClicked(data) {
            // course name of checkbox will be passed through as the data variable
            if (this.changeTabOnSelection) {
                this.tab += 1
            }

            let children = this.$refs[data.ref]
            // if the course has been selected, go into all of the other coursetables of the same ref
            //  and make sure that they are also checked. Otherwise, deselect them.

            children.forEach((child) => {
                child.$children
                    .filter(
                        (c) =>
                            c.$options._componentTag === 'CourseTableCourse' &&
                            c.course.name === data.name
                    )
                    .map((c) => c.setSelected(data.selected))
            })
        },
        deselectCourses() {
            let pathway = this.$store.state.pathways[this.pathwayID]
            pathway.courses.forEach((course) => {
                const c = { pathwayID: this.pathwayID, course: course }
                // delete course
                this.$store.commit('delCourse', c)
            })
            // deselect course
            for (const i in this.classTabs) {
                this.$refs[i][0].deselectAll()
            }
            /* <!-- ! this is sus -->
             * this WILL break with the current implementation of graph view
             *  because this.$refs[tab] gives me an array of all of the courseTable components
             *   on the DOM. Right now, there is only one, but with the current implementation
             *    of graph view, there will be more courseTable components which will make the
             *     array that this.$refs[tab] gives have multiple couresTable elements
             *      this should be revamped in the future to change how I deselect courses
             *
             * this should be changed in the future
             */
        },
        toggleGraph() {
            // console.log(this.courses);
            this.showGraph = !this.showGraph
        },
        resize(left, right) {
            // console.log(this.priorities)
            let containers = Object.keys(this.priorities);
            containers = containers.filter( p => this.priorities[p] )
            // console.log(containers)
            console.log(this.$refs)
            let resized = [ left/(right + left), right/(right + left )];
            // console.log(resized)
            // this.$refs.tab[0].style.flexBasis = `${resized[1]*100}%`;
            this.$refs.tab.forEach( (tab, index) => {
                console.log(tab);
                tab.style.flexBasis = `${resized[1-index]*100}%`;
            })
            // containers.forEach( (id, index) => {
            //     document.getElementById(id).style.flexBasis = resized[index];
            //     // if ( index == 0 ) console.log(el.style.flexBasis)
                
            //     // // el.style.flexBasis = `${resized[index]}`;
            //     // if ( index == 0 ) console.log(el.style.flexBasis)
            // })
        },
        getWidth(key) {
            this.debug();
        }

    },
}
</script>

<style scoped>
#graphView {
    /* border: 1px solid fuchsia; */
    display: flex;
    flex-wrap: wrap;
    justify-content: normal;
    flex-direction: row;
}
#graphView > .tab {
    flex: 1 1 160px;
    margin: 0 2%;
    /* border: 1px red solid; */
}
.tab {
    display: flex;
    flex-wrap: nowrap;
    flex-direction: column;
    border: 1px solid gray;
    border-radius: 5%;
    box-sizing: border-box;
    padding: 5px;
    margin: 0 auto;
}
.courseTitle {
    margin: 0 auto;
    font-weight: bolder;
}
#graphTabs {
    /* flex: 1 1 20vw; */
    display: flex;
    flex: auto;
    /* max-width: 20vw; */
}

.graph-fab-container {
    position: fixed;
    right: 40px;
    bottom: 20px;
    width: 56px;
    height: 90px;
    z-index: 999;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.header h1 {
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

/* @media only screen and (min-width: 600px) {
    .fab-container {
        right: 50px;
        bottom: 50px;
    }
} */
</style>
