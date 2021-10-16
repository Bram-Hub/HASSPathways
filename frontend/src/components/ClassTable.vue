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
            >
                Open / Close All
            </v-btn>

            <v-divider vertical class="mx-4" />

            <v-btn
                color="primary"
                depressed
                elevation="1"
            >
                <v-icon left dark>
                    mdi-trash-can-outline
                </v-icon>
                Clear selection
            </v-btn>
        </v-card>
      
        <v-data-table
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
            fixed-header
            class="elevation-1 class-data-table"

            @click:row="(item, slot) => slot.expand(!slot.isExpanded)"
        >
            <template #item.data-table-select="{isSelected,select}">
                <v-simple-checkbox v-ripple color="blue" :value="isSelected" @input="select($event)" />
            </template>
    
            <!-- Remove select all / unselect all button to prevent
                 users accidentally clearing their selections -->
            <template #header.data-table-select="{ item }" />

            <template #item.modifiers="{ item }">
                <v-chip
                    :color="red"
                >
                    <v-icon color="blue darken-2">
                        mdi-weather-sunny
                    </v-icon>
                </v-chip>
                <v-chip>
                    <v-icon color="blue darken-2">
                        mdi-leaf-maple
                    </v-icon>
                </v-chip>
                <v-chip>
                    <v-icon color="blue darken-2">
                        mdi-flower-poppy
                    </v-icon>
                </v-chip>

                <!-- DI = data intensive, communication intensive, hass inqury -->

                <v-chip
                    v-for="modifier in item.modifiers.filter(modifier => !['summer', 'spring', 'fall'].includes(modifier))"
                    :key="modifier"

                    :color="red" dark
                >
                    {{ modifier }}
                </v-chip>
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
export default {
    name: 'ClassTable',

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
            classes.push({
                name: 'Made Up Class',
                prefix: 'BRT' + Math.floor(Math.random() * 10),
                id: Math.floor(Math.random() * 5000) + 1000,
                description: "What is science, what is technology, and how have these two fields of inquiry evolved over time? This course examines these questions by studying the history of various scientific fields and technologies. In addition to tracing the historical evolution of the topics studied, the course will consider how social, political, economic and cultural factors helped to shape \u2013 and were in turn shaped by \u2013 advances in science and technology. The course will also reflect upon the relationship between science and technology on the one hand, and \u201cprogress\u201d on the other.",
                modifiers: ['CI', 'DI', 'HI', 'fall', 'spring', 'summer', 'major_restricted']
            });
        }
        
        return {
            search: '',
            show_search_bar: true,
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
        rowClass() { return 'expandable-table-row'; }
    }
}
</script>

<style>
/* TODO move to global css */
.expandable-table-row {
    cursor: pointer;
}

.v-data-table > .v-data-table__wrapper tbody tr.v-data-table__expanded__content {
    box-shadow: inset 0px 0px 1px 0px rgba(0,0,0,0.25);
}

.theme--light.v-data-table tbody tr.v-data-table__selected {
    background-color: #E3F2FD;
}

.class-data-table tr th:nth-child(2),
.class-data-table tr td:nth-child(2) {
    padding-right: 0px !important;
}


.class-data-table tr th:nth-child(3),
.class-data-table tr td:nth-child(3) {
    padding-left: 4px !important;
}
</style>

<style scoped>
.class-desc-container {
    padding: 16px;
}
</style>