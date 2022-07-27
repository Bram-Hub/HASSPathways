<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <YearSelection />

            <h1>My HASS Pathways</h1>

            <p>
                Select a pathway below to get started, or <router-link to="/search-classes">
                    choose a pathway from the classes you've taken
                </router-link>
            </p>

            <v-divider class="my-4" />

            {{ currentRouteName }}
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'
import YearSelection from '../../components/YearSelection.vue'

export default {
    components: {
        Breadcrumbs, YearSelection
    },
    props: {
        path: {
            default: '',
            type: String,
        },
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.my_pathway_template.map(x => x || {
                text: 'hello',
                href: ''
            })
        }
    },
    computed: {
        currentRouteName() {
            return this.$route.query;
        }
    }
}
</script>
