<template>
    <div>
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <h1>Search for the classes you have taken and then continue to the next page to display the computed pathways for you!</h1>
        <h3>Type in the name of the course or the course ID to search for the courses you have taken</h3>

        <input id="search-input" v-model="searchValue" type="text" placeholder="Search Class" />
        <div v-for="course in filteredCourses" :key="course.name">
                    <input id="course.id" type="checkbox" v-model="checkedCourses" :value="course.name">
            <label for="course.name"> {{ course.name + ", " + course.prefix + "-" + course.ID}} </label>
        </div>
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
            breadcrumbs: breadcrumbs.pathway_from_classes,
            searchValue: '',
            checkedCourses: []
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
    }
}
</script>
