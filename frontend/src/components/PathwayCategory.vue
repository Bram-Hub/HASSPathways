<template>
    <v-card class="card" elevation="1">
        <v-img
            height="76px"
            class="card-img"
            :src="require('../assets/pathway-groups/' + image)"
        >
            <div class="darken" />

            <v-card-title class="font-weight-bold text-truncate card-title">
                {{ title }}
            </v-card-title>
        </v-img>
        
        <ul class="pathways-container">
            <v-tooltip
                v-for="pathway in filteredPathways"
                :key="pathway"

                bottom
                eager
                color="black"
                offset-overflow
                max-width="400px"
                open-delay="700"
                transition="none"
            >
                <template #activator="{ on, attrs }">
                    <li class="pathway" v-bind="attrs" v-on="on">
                        <a :href="`/pathway?pathway=${encodeURIComponent(pathway)}`" class="text-decoration-none">
                            <b>{{ pathway }}</b>
                        </a>
                    </li>
                </template>
                <span v-if="pathwaysData[pathway]">{{ pathwaysData[pathway].description }}</span>
            </v-tooltip>
        </ul>
    </v-card>
</template>

<script>

export default {
    name: 'PathwayCategory',
    props: {
        title: {
            type: String,
            required: true
        },
        text: {
            type: String,
            required: true
        },
        image: {
            type: String,
            default: ''
        },
        pathways: {
            type: Array, // Array of pathway ids
            default: () => [],
        }
    },
    data() { return { pathwaysData: {} }; },
    computed: {
        filteredPathways() {
            let output = [];
            for(const pathway in this.pathways) {
                if(this.pathwaysData[this.pathways[pathway]]) {
                    output.push(this.pathways[pathway])
                }
            }
            return output;
        }
    },
    created() {
        const year = this.$store.state.year;
        import('../data/json/' + year + '/pathways.json').then((val) => this.pathwaysData = Object.freeze(val));
    }
}
</script>

<style scoped lang="scss">



.bookmark-holder:hover {
    cursor: pointer;
}
.card {
    width: 100%;
    max-width: calc(100vw - 24px);
    display: inline-block;
    vertical-align: top;
}

.darken {
    width: 100%;
    height: 100%;
    background-color: DarkSlateGray;
    opacity: 0.4;
    transition: opacity 0.2s;
}

.card:hover .darken {
    opacity: 0.1;
    transition: opacity 0.2s;
}

.card-title {
    color: white;
    position: absolute;
    bottom: 0;
    display: block;
    width: 100%;
}

.pathways-container {
    overflow-y: auto;
    margin: 10px 0;
    list-style-type: square;
}

.pathway {
    padding: 6px 4px;
    margin-left: 8px;
    cursor: pointer;
    font-size: 0.875em;
}

.pathway:hover h4 {
    text-decoration: underline;
}

.pathway:last-child {
    border-bottom: none;
}
</style>
