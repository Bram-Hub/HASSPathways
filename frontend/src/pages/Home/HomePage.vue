<template>
    <div>
        <v-container>
            <h1>HASS Pathways</h1>

            <v-divider class="my-4" />

            <p>Select a pathway below to get started, or <a>choose a pathway from the classes you've taken</a></p>

            <PathwayCategory 
                v-for="item in pathway_categories"
                :key="item.name"
                :title="item.name"
                :image="item.image"
                :text="item.name"
                :pathways="item.pathways"
            />
        </v-container>
    </div>
</template>

<script>
import PathwayCategory from '../../components/PathwayCategory'

const pathway_categories = require('../../../data/pathway-categories');

export default {
    components: {
        PathwayCategory
    },
    props: {
        path: {
            default: '',
            type: String,
        },
    },
    data: () => { return { pathway_categories }; },
}
</script>


