<template>
    <v-container style="min-height: 50vh">
        <!-- Table header with search and open/close all buttons
          -- A scale transform is applied to make it smaller -->
        <v-card
            class="table-header-search elevation-0 ( pt-2 pb-2 pr-4 ) d-flex" 
        > 
            <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                outlined
                dense
                hide-details
                class="ma-0"
                style="width: 400px; max-width: 100%"
            />
        </v-card>

        <ClassTableClass 
            v-for="item in filteredClasses" 
            :key="item.prefix + item.ID" 
            :clazz="item"
            :pathway-id="pathwayId"
        />

        <p v-if="filteredClasses.length === 0" class="no-search-results">
            No search results
        </p>
    </v-container>
</template>

<script>
import ClassTableClass from './ClassTableClass'
import search from '../helpers/search-classes.js'

export default {
    name: 'ClassTable',
    components: { ClassTableClass },
    props: {
        classes: {
            type: Array,
            required: true
        },
        pathwayId: {
            type: String,
            required: false,
            default: null
        }
    },
    data() {
        return { search: '' }
    },
    computed: {
        filteredClasses() {
            return search(this.classes, this.search);
        }
    },
    methods: {
        deselectAll() {
            this.$children.forEach(child => {
                if (child.setSelected) child.setSelected(0);
            });
        },
        getSelected() {
            return this.$children
                .filter(child => child.setSelected)
                .map(child => child.key);
        }
    }
}
</script>

<style scoped>
.table-header-search {
    transform: scale(0.8);
    transform-origin: bottom left;
}

.no-search-results {
    margin: 20px 5px;
}
</style>
