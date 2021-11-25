<template>
    <v-container>
        <!-- Table header with search and open/close all buttons
          -- A scale transform is applied to make it smaller -->
        <v-card
            class="table-header-search ( elevation-1 rounded-0 ) ( pt-4 pb-2 pr-4 ) d-flex" 
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
        />
    </v-container>
</template>

<script>
import ClassTableClass from './ClassTableClass'

export default {
    name: 'ClassTable',
    components: { ClassTableClass },
    props: {
        classes: {
            type: Array,
            required: true
        }
    },
    data() {
        return { search: '' }
    },
    computed: {
        filteredClasses() {
            if (!this.search)
                return this.classes;

            let words = this.search
                .toLowerCase()
                .replace(/([A-Za-z]{4})-(\d{4})/, '$1 $2')
                .split(' ')
    
            return this.classes.filter(clazz => {
                return words.some(word =>
                    (`${clazz.name} ${clazz.ID} ${clazz.prefix} ${clazz.description}`)
                        .toLowerCase()
                        .includes(word));
            });
        }
    },

    methods: {
        deselectAll() {
            this.$children.forEach(child => {
                if (child.setSelected) child.setSelected(0);
            });
        }
    }
}
</script>

<style scoped>
.table-header-search {
    transform: scale(0.8);
    transform-origin: bottom left;
}
</style>
