<template>
    <v-container>
        <v-card
            v-if="show_search_bar"
            class="elevation-1 rounded-0 pt-4 pb-2 px-4 d-flex" 
            style="transform: scale(0.8); transform-origin: bottom left;"
        > 
            <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                outlined
                dense
                hide-details
                class="ma-0"
                style="width: 500px; max-width: 100%"
            /> <!-- TODO: classes / dynamic mobile -->

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
                        <h3 class="mb-1">Are you sure?</h3>
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
            </v-dialog>
        </v-card>
      
        <v-data-table
            ref="data-table"
            :headers="headers"
            :items="classes"
            :sort-by.sync="sortBy"
            :sort-desc.sync="sortDesc"
            :expanded.sync="expanded"
            :item-class="rowClass"

            :search="search"
            item-key="id"
            show-select
            show-expand
            hide-default-footer
            disable-pagination
            fixed-header
            class="elevation-1 class-data-table"

            @click:row="(item, slot) => slot.expand(!slot.isExpanded)"
        >
            <template #item.data-table-select="{isSelected,select}">
                <v-simple-checkbox v-ripple color="primary" :value="isSelected" @input="select($event)" />
            </template>
    
            <!-- Remove select all / unselect all button to prevent
                 users accidentally clearing their selections -->
            <template #header.data-table-select="{ item }" />

            <template #item.modifiers="{ item }">
                <ClassTableModifiers :item="item" />
            </template>

            <template #expanded-item="{ headers, item }">
                <td :colspan="headers.length">
                    <div class="class-desc-container">
                        More info about {{ item.description }}
                    </div>
                </td>
            </template>
        </v-data-table>
    </v-container>
</template>

<script>
import ClassTableModifiers from './ClassTableModifiers'

export default {
    name: 'ClassTable',
    components: {
        ClassTableModifiers
    },

    data() {
        let classes = [
            {
                name: 'Art History',
                prefix: 'ARTS',
                id: 4350,
                description: "What is science, what is technology, and how have these two fields of inquiry evolved over time? This course examines these questions by studying the history of various scientific fields and technologies. In addition to tracing the historical evolution of the topics studied, the course will consider how social, political, economic and cultural factors helped to shape \u2013 and were in turn shaped by \u2013 advances in science and technology. The course will also reflect upon the relationship between science and technology on the one hand, and \u201cprogress\u201d on the other.",
                modifiers: ['CI', 'DI', 'HI', 'fall', 'spring', 'summer', 'major_restricted']
            },
            {
                name: 'Made Up Class',
                prefix: 'BRTS',
                id: 2350,
                description: "What is science, what is technology, and how have these two fields of inquiry evolved over time? This course examines these questions by studying the history of various scientific fields and technologies. In addition to tracing the historical evolution of the topics studied, the course will consider how social, political, economic and cultural factors helped to shape \u2013 and were in turn shaped by \u2013 advances in science and technology. The course will also reflect upon the relationship between science and technology on the one hand, and \u201cprogress\u201d on the other.",
                modifiers: ['CI', 'DI', 'HI', 'fall', 'spring', 'summer', 'major_restricted']
            },
        ];

        for (let i = 0; i < 20; i++) {
            let m = [];

            ['CI', 'DI', 'HI', 'fall', 'spring', 'summer', 'major_restricted']

            let x = Math.random() * 7;
            for (let i = 0; i < x; i++) {
                let y = ['CI', 'DI', 'HI', 'fall', 'spring', 'summer', 'major_restricted'];
                let z = y[Math.floor(y.length * Math.random())]
                if (!m.includes(z))
                    m.push(z);
            }

            classes.push({
                name: 'Made Up Class',
                prefix: 'BRT' + Math.floor(Math.random() * 10),
                id: Math.floor(Math.random() * 5000) + 1000,
                description: "What is science, what is technology, and how have these two fields of inquiry evolved over time? This course examines these questions by studying the history of various scientific fields and technologies. In addition to tracing the historical evolution of the topics studied, the course will consider how social, political, economic and cultural factors helped to shape \u2013 and were in turn shaped by \u2013 advances in science and technology. The course will also reflect upon the relationship between science and technology on the one hand, and \u201cprogress\u201d on the other.",
                modifiers: m
            });
        }
        
        return {
            search: '',
            dialog: false,
            show_search_bar: true,
            global_expanded: false,
            global_expanded2: false,
            headers: [
                { text: 'Pfx', value: 'prefix', width: '60px' },
                { text: 'Lvl', value: 'id', width: '60px' },
                { text: 'Name', value: 'name' },
                { text: 'Modifiers', value: 'modifiers', align: 'right' },
                { value: 'data-table-select' }
            ],
            classes: classes
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
    }
}
</script>

<style lang="scss">
@import "../styles/_data-tables.scss";
</style>

<style scoped>
.class-desc-container {
    padding: 16px;
}
</style>