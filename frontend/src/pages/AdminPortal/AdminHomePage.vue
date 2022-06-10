<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Welcome to the Admin Portal!</h1>
            <p>Here you can edit the courses and pathways on the website!</p>

            <v-divider class="my-4" />

            <ul>
                <li v-bind="attrs" v-on="on">
                    <router-link
                        :to="{ name: 'admin-pathway' }"
                        class="text-decoration-none"
                    >
                        Search for a class by pathway.
                    </router-link>
                </li>
                <li v-bind="attrs" v-on="on">
                    <router-link
                        :to="{ name: 'admin-search-course-code' }"
                        class="text-decoration-none"
                    >
                        Edit a class by course code.
                    </router-link>
                </li>
                <li v-bind="attrs" v-on="on">
                    <router-link
                        :to="{ name: 'admin-course' }"
                        class="text-decoration-none"
                    >
                        Add a new course to the website.
                    </router-link>
                </li>
            </ul>
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
