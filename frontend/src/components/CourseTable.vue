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
        }
    },
    data() {
        return { search: '' }
    },
    // watch: {
    //     descriptionOnHover( newValue ) {
    //         console.log(`old value: ${this.descriptionOnHover} new value: ${newValue}`);
    //     }
    // },
    computed: {
        filteredCourses() {
            let tempCourses = JSON.parse(JSON.stringify(this.courses));

            if(this.search && this.search != ''){
                tempCourses = Object.fromEntries(Object.entries(tempCourses)
                    .filter(([key]) => key
                        .toUpperCase()
                        .includes(this.search.toUpperCase())));
            }
            for(const course in tempCourses) {
                if(tempCourses[course] == null) {
                    tempCourses[course]= {};
                    tempCourses[course]["name"] = course;
                    tempCourses[course]["hasData"] = false;
                }
                else {
                    tempCourses[course]["hasData"] = true;
                }
            }

            tempCourses = Object.values(tempCourses).sort(
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
            return tempCourses
        }
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
</style>
