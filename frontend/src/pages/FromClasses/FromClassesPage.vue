<template>
    <div>
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <h1>Search for the classes you have taken and then continue to the next page to display the computed pathways for you!</h1>
        <h3>Type in the name of the course or the course ID to search for the courses you have taken</h3>
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
            searchValue: ''
        }
    },
    computed: {
        filteredCourses() {
            let tempCourses = courses;

            if(this.searchValue != '' && this.searchValue) {
                tempCourses = tempCourses.filter((item) => {
                    let combinedID = item.prefix + '-' + item.ID;
                    return item.name
                    .toUpperCase()
                    .includes(this.searchValue.toUpperCase()) ||
                    combinedID
                    .toUpperCase()
                    .includes(this.searchValue.toUpperCase());
                })
            }

            return tempCourses;
        }
    }
}
</script>
