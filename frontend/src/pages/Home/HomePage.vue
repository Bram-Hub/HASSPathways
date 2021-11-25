<template>
    <div>
        <v-container>
            <h1>HASS Pathways</h1>
            <p>Select a pathway below to get started, or <a>choose a pathway from the classes you've taken</a></p>

            <v-divider class="my-4" />

            <div class="pathway-categories">
                <PathwayCategory 
                    v-for="item in pathwayCategories"
                    :key="item.name"
                    :title="item.name"
                    :image="item.image"
                    :text="item.name"
                    :pathways="item.pathways"
                />
            </div>
        </v-container>
    </div>
</template>

<script>
import PathwayCategory from '../../components/PathwayCategory'
import { pathwayCategories } from '../../data/data.js'

export default {
    components: { PathwayCategory },
    data: () => { return { pathwayCategories }; },
}
</script>

<style scoped>
.pathway-categories {
    max-width: 100vw;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    grid-gap: 10px;
}
</style>
