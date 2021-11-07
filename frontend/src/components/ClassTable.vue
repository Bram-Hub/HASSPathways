<template>
    <v-container>
        <!-- Table header with search and open/close all buttons
          -- A scale transform is applied to make it smaller -->
        <v-card
            v-if="show_search_bar"
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
import ClassTableModifiers from './ClassTableModifiers'
import ClassTableClass from './ClassTableClass'

export default {
    name: 'ClassTable',
    components: {
        ClassTableClass
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
                name: 'Made Up Class' + (Math.random() < 0.5 ? ' Extra long super exenobiology studies' : ''),
                prefix: 'BRT' + Math.floor(Math.random() * 10),
                id: Math.floor(Math.random() * 5000) + 1000,
                description: Math.random() < 0.5 ?
                    "What is science, what is technology, and how have these two fields of inquiry evolved over time? This course examines these questions by studying the history of various scientific fields and technologies. In addition to tracing the historical evolution of the topics studied, the course will consider how social, political, economic and cultural factors helped to shape \u2013 and were in turn shaped by \u2013 advances in science and technology. The course will also reflect upon the relationship between science and technology on the one hand, and \u201cprogress\u201d on the other."
                    : "This course assumes no previous knowledge of the subject. The course is designed to provide students with fundamental skills in listening, speaking, reading, and writing Mandarin Chinese. Oral and aural skills will be emphasized. Background on Chinese culture will be introduced as an element of the course. For entry level, non-native speakers only.",
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