<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Search for the classes to edit!</h1>
            <h3>Type in the name of the course or the course ID to search for the courses you have taken</h3>
            <div class="search-field">
                <v-text-field
                    v-model="searchValue"
                    outlined
                    rounded
                    solo
                    label="Search Class"
                    class="search-field"
                />
            </div>
            <div v-for="course in filteredCourses" :key="course.name">
                <v-btn
                    :id="course.name"
                    :to="`/admin-portal/course?class=${encodeURIComponent(course.name.slice().toLowerCase().replace(/ /g, '_'))}`"
                >
                  Edit
                </v-btn>
                <label class="label" :for="course.name"> {{ course.name + ", " + course.prefix + "-" + course.ID }} </label>
                <div>
                    <v-dialog>
                        <template #activator="on">
                            <v-btn color="red" v-on="on">
                                Remove
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-text>
                                Are you sure you want to delete this course?
                            </v-card-text>
                            <v-card-actions>
                                <v-btn @click="remove(course)">
                                    Yes
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </div>
            </div>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'
import { courses } from '../../data/data.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.admin_search_cc_page,
            searchValue: ''
        }
    },
    computed: {
        filteredCourses() {
            let tempCourses = Object.entries(courses);

            if(this.searchValue != '' && this.searchValue) {
                tempCourses = tempCourses.filter((item) => {
                    let combinedID = item[1].prefix + '-' + item[1].ID;

                    return item[1].name
                        .toUpperCase()
                        .includes(this.searchValue.toUpperCase()) ||
                        combinedID
                            .toUpperCase()
                            .includes(this.searchValue.toUpperCase());
                })
            }
            return Object.fromEntries(tempCourses);
        }
    },
    methods: {
        remove(course) {
            console.log(course)
        }
    }
}
</script>
<style>
    .label {
        border: 1px solid #666;
        padding: 10px 15px;
        text-align: center;
        display: inline-block;
        font-size: 15px;
        margin: 5px;
        cursor: pointer;
        }
    .search-field {
        width: 400px;
    }
</style>
