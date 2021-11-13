<template>
    <v-container>
        <!-- Table header with search and open/close all buttons
          -- A scale transform is applied to make it smaller -->
        <v-card
            class="table-header-search elevation-1 rounded-0 pt-4 pb-2 px-4 d-flex" 
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
            /> <!-- TODO: classes / dynamic mobile -->

            <!--
            <v-divider vertical class="mx-4" />

            <v-btn
                color="primary"
                depressed
                elevation="1"
                @click="toggleAll()"
            >
                <v-icon left dark>
                    {{ global_expanded2 ? 'mdi-folder-open' : 'mdi-folder' }}
                </v-icon>
                Open / Close All
            </v-btn>

            <v-divider vertical class="mx-4" />

            <v-dialog
                v-model="dialog"
                width="500"
                light
                overlay-opacity="0.8"
            >
                <template #activator="{ on, attrs }">
                    <v-btn
                        color="primary"
                        depressed
                        elevation="1"    

                        v-bind="attrs"
                        v-on="on"
                    >
                        <v-icon left dark>
                            mdi-trash-can-outline
                        </v-icon>
                        Clear selection
                    </v-btn>
                </template>

                <v-card>
                    <v-card-text class="pt-4">
                        <h3 class="mb-1">
                            Are you sure?
                        </h3>
                        You are about to unselect all your classes for this tab[TODO tab name]
                    </v-card-text>

                    <v-divider />

                    <v-card-actions>
                        <v-spacer />
                        <v-btn
                            color="primary"
                            text
                            @click="dialog = false"
                        >
                            Cancel
                        </v-btn>

                        <v-btn
                            color="primary"
                            text
                            @click="deselectAll(); dialog = false"
                        >
                            Unselect all
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog> -->
        </v-card>

        <v-btn @click="test()">Test</v-btn>
      
        <ClassTableClass 
            v-for="item in filteredClasses" 
            :key="item.prefix + item.id" 
            :clazz="item"
        />

        <!-- The data table itself -->
    </v-container>
</template>

<script>
import ClassTableClass from './ClassTableClass'

export default {
    name: 'ClassTable',
    components: {
        ClassTableClass
    },

    props: {
        classes: {
            type: Array,
            required: true
        }
    },

    data() {
        return {
            search: ''
        }
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
                    (`${clazz.name} ${clazz.id} ${clazz.prefix} ${clazz.description}`)
                        .toLowerCase()
                        .includes(word));
            });
        }
    },

    methods: {
        rowClass() { return 'expandable-table-row'; },
        toggleAll () {
            this.global_expanded = !this.global_expanded;
            this.$refs['data-table'].expanded =
                this.global_expanded ? this.classes : [];
            setTimeout(() => this.global_expanded2 = this.global_expanded, 30);
        },
        test() {
            console.log(this.$children)
            this.$children.forEach(child => {
                if (child.setSelected) child.setSelected(1);
            });
        }
    }
}
</script>

<style lang="scss">
@import "../styles/_data-tables.scss";

.table-header-search {
    transform: scale(0.8);
    transform-origin: bottom left;
}
</style>

<style scoped>
.class-desc-container {
    padding: 16px;
}
</style>