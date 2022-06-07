<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Welcome to the Admin Portal!</h1><h3>Here you can edit the courses and pathways on the website!</h3>
            <v-btn
                class="button"
                elevation="0"
                tile
                :to="{ name: 'admin-pathway' }"
            >
                <span class="text">Search for a class by pathway!</span>
            </v-btn>
            <v-btn
                class="button"
                elevation="0"
                tile
                :to="{ name: 'admin-search-course-code' }"
            >
                <span class="text">Search for a class to edit by course code.</span>
            </v-btn>
            <v-btn
                class="button"
                elevation="0"
                tile
                :to="{ name: 'admin-course' }"
            >
                <span class="text">Add a new course to the website!</span>
            </v-btn>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.admin_home_page
        }
    }
}
</script>
