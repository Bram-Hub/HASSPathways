<template>
    <v-container :class="{ minHeight : !graph}">
        <!-- Table header with search and open/close all buttons
          -- A scale transform is applied to make it smaller -->
        <v-card
            v-if="searchBar"
            class="table-header-search elevation-0 ( pt-2 pb-2 pr-4 ) d-flex"
        > 
            <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                outlined
                dense
                hide-details
                class="ma-0"
                style="width: 400px; max-width: 100%"
            />
            <div id class="SORT"> 
                <!-- search bar -->
                <v-select 
                    v-model="advanced_search" 
                    dense
                    :items="sort_dropbox" 
                    multiple
                    outlined
                    chips
                    label = "Sort" 
                    clearable
                    style="width: 275px; max-width: 100%; z-index: 100"
                    >
                    <template v-slot:selection="{ item, index }">
                        <v-chip v-if="index === 0">
                            <span>{{ item }}</span>
                        </v-chip>
                        <span
                            v-if="index == 1"
                            class="grey--text text-caption"
                        >
                            (+{{ advanced_search.length - 1 }} others)
                        </span>
                    </template>
                </v-select> 

            </div>
        </v-card>
        <div :class="{graphContainer: graph}">
            <CourseTableCourse
                v-for="item in filteredCourses"
                :key="item.name"
                :course="item"
                :pathway-id="pathwayId"
                :desc="desc"
                :hover="hover"
                :graph="graph"
                @checkbox-clicked="update"
            />
        </div>


        <p v-if="filteredCourses.length === 0" class="no-search-results">
            No search results
        </p>
    </v-container>
</template>

<script>
import CourseTableCourse from './CourseTableCourse'

export default {
    name: 'CourseTable',
    components: { CourseTableCourse },
    props: {
        category: {
            type: String,
            required: true
        },
        courses: {
            type: Object,
            required: true
        },
        pathwayId: {
            type: String,
            required: false,
            default: null
        },
        desc: {
            type: Boolean,
            required: false,
            default: true,
        },
        hover: {
            type: Boolean,
            required: false,
            default: false,
        },
        searchBar: {
            type: Boolean,
            required: false,
            default: true,
        },
        graph: {
            type: Boolean,
            required: false,
        },
        hasData: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {    advanced_search: [],
                    search: '' ,
                    sort_dropbox: ['Fall', 'Spring', 'Summer', 'CI','HI', 'No Prerequistes'],
        }
    },
    // watch: {
    //     descriptionOnHover( newValue ) {
    //         console.log(`old value: ${this.descriptionOnHover} new value: ${newValue}`);
    //     }
    // },
    computed: {
        filteredCourses() {
            let tempCourses = JSON.parse(JSON.stringify(this.courses));
            console.log(tempCourses);
            let output = [];
            //Weird hack that is needed
            //Basically since this is a computed method it will auto run
            //whenever the "data" is changed but since this.courses
            //doesn't change since it is a reference to the courses from
            //the parent component we need to change a data piece that
            //is used in this function. I created the hasData prop to do 
            //this. We need to then use the hasData to do "something"
            //in order for it to be rerendered, I used an arbitrary if
            //statement that will have no effect in order to compile with 
            // no warnings.
            if(this.hasData) {
                tempCourses = JSON.parse(JSON.stringify(tempCourses));
            }

            if(this.search && this.search != ''){
                tempCourses = Object.fromEntries(Object.entries(tempCourses)
                    .filter(([key]) => key
                        .toUpperCase()
                        .includes(this.search.toUpperCase())));
            }

            console.log(tempCourses);

            for(const course in tempCourses) {
                if(tempCourses[course] == null) {
                    tempCourses[course] = {};
                    tempCourses[course]["name"] = course;
                    tempCourses[course]["hasData"] = false;
                }
                else {
                    tempCourses[course]["hasData"] = true;
                }
                //Check if there is data for the course
                if (this.advanced_search.length > 0 && !tempCourses[course].hasData) {
                    continue
                }
                //Check fall
                if (this.advanced_search.includes("Fall") && !tempCourses[course].offered.fall) {
                    continue;
                }
                //Check spring
                if (this.advanced_search.includes("Spring") && !tempCourses[course].offered.spring) {
                    continue;
                }
                //Check summer
                if (this.advanced_search.includes("Summer") && !tempCourses[course].offered.summer) {
                    continue;
                }
                 if (this.advanced_search.includes("HI") && !tempCourses[course].properties.HI) {
                    continue;
                 }
                //check prereq
                if (this.advanced_search.includes("No Prerequistes") && tempCourses[course].prerequisites.length != 0) {
                    continue;
                }
                //Check CI
                if (this.advanced_search.includes("CI") && !tempCourses[course].properties.CI) {
                    continue;
                }
                output.push(tempCourses[course]);
            }

            output = Object.values(output).sort(
                function(a, b){
                    if(a.subj === undefined) return  1
                    if(b.subj === undefined) return -1
                    if(a.ID === undefined)   return  1
                    if(b.ID === undefined)   return -1
                    if(a.ID == b.ID){
                        if(a.subj < b.subj) return -1
                        else                return 1
                    } else if (a.ID < b.ID) return -1
                    else return 1
                }
            )
            return output;
        },

    },

    methods: {
        deselectAll() {
            this.$children.forEach(child => {
                if (child.setSelected) child.setSelected(0);
            });
        },
        update( data ) {   
            data.ref = this.category;
            // data: { name: course name, selected: true/false, category: "One Of"/"Remaining"/... }
            this.$emit('checkbox-clicked', data);
        }
    }
}
</script>

<style scoped>

.minHeight {
    min-height: 50vh;
}
.graphContent {
    display: flex;
    width: 100%;
    flex-wrap: wrap;
}

.graph-content CourseTableCourse {
    margin: 0;
}
.graphContainer {
    display: flex;
    flex: 50%;
    flex-wrap: wrap;
    margin: 0 auto;
    justify-content: center;
    
}
.graphContainer * {
    width: 300px;
    margin: 5px 5px;
    flex-grow: 1;
}
.table-header-search {
    transform-origin: bottom left;
}

.no-search-results {
    margin: 20px 5px;
}

.SORT {
    padding-bottom: 1 px;
}
</style>