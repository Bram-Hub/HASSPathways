<template>
    <v-container style="min-height: 50vh">
        <!-- Table header with search and open/close all buttons
          -- A scale transform is applied to make it smaller -->
        <div style="max-width: 700px;">
            <v-card
                class="table-header-search elevation-0 ( pt-2 pb-2 ) d-flex"
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

            <CourseTableCourse
                v-for="item in filteredCourses"
                :key="item.name"
                :course="item"
                :pathway-id="pathwayId"
                @checkbox-clicked="$emit('checkbox-clicked')"
            />

            <p v-if="filteredCourses.length === 0" class="no-search-results">
                No search results
            </p>
        </div>
    </v-container>
</template>

<script>
import CourseTableCourse from './CourseTableCourse'

export default {
    name: 'CourseTable',
    components: { CourseTableCourse },
    props: {
        courses: {
            type: Object,
            required: true
        },
        pathwayId: {
            type: String,
            required: false,
            default: null
        }
    },
    data() {
        return { search: '' }
    },
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
            return tempCourses;
        }
    },
    methods: {
        deselectAll() {
            this.$children.forEach(child => {
                if (child.setSelected) child.setSelected(0);
            });
        }
    }
}
</script>

<style scoped>
.table-header-search {
    transform-origin: bottom left;
}

.no-search-results {
    margin: 20px 5px;
}
</style>
