<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />

            <h1>My HASS Pathways</h1>

            <p>Select a pathway below to get started, or <a>choose a pathway from the classes you've taken</a></p>

            <v-divider class="my-4" />

            {{ currentRouteName }}
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
