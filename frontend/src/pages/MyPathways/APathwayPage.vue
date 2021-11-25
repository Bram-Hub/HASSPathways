<template>
    <div>
        <v-container>
            <v-breadcrumbs :items="breadcrumbs" class="px-0">
                <template #divider>
                    <v-icon>mdi-chevron-right</v-icon>
                </template>
            </v-breadcrumbs>

            <h1>My HASS Pathways</h1>

            <p>Select a pathway below to get started, or <a>choose a pathway from the classes you've taken</a></p>

            <v-divider class="my-4" />

            {{ currentRouteName }}
        </v-container>
    </div>
</template>

<script>
import MyPathway from '../../components/MyPathway'

export default {
    components: {
        
    },
    props: {
        path: {
            default: '',
            type: String,
        },
    },
    data() {
        return {
            breadcrumbs: [
                {
                    text: 'Dashboard',
                    disabled: false,
                    href: 'breadcrumbs_dashboard',
                },
                {
                    text: 'Link 1',
                    disabled: false,
                    href: 'breadcrumbs_link_1',
                },
                {
                    text: 'Link 2',
                    disabled: true,
                    href: 'breadcrumbs_link_2',
                },
            ],
        }
    },
    computed: {
        currentRouteName() {
            return this.$route.query;
        }
    }
}
</script>
