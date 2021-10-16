<template>
    <v-card class="rounded-0 card" elevation="1">
        <v-img
            height="86px"
            class="card-img"
            :src="require('../assets/pathway-groups/' + image)"
        >
            <div class="darken" />
            <v-card-title class="font-weight-bold text-truncate card-title">
                {{ title }}
            </v-card-title>
        </v-img>
        
        <div class="pathways-container">
            <a href="" class="text-decoration-none">
                <div
                    v-for="pathway in pathways" :key="pathway"
                    class="pathway"
                >
                    <h4>{{ pathway }}</h4>
                    <p class="mb-0 d-block text-truncate">This is a sample description (TODO later)</p>
                </div>
            </a>
        </div>
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
            type: Array,
            default: () => []
        }
    }
}
</script>

<style scoped>
    .card {
        margin: 5px;
        width: 340px;
        max-width: 95%;

        display: inline-block;
        vertical-align: top;
    }

    .pathways-container {
        height: 350px;
        overflow-y: auto;
        margin-top: 10px;
    }

    .pathway {
        padding: 3px 16px;
        cursor: pointer;
        font-size: 0.875em;
        border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    }

    .pathway:hover {
        background-color: #fafafa;
    }

    .pathway:hover > h4 {
        text-decoration: underline;
    }

    .pathway > p {
        color: #222;
    }
    
    .pathway:last-child {
        border-bottom: none;
    }

    .darken {
        width: 100%;
        height: 100%;
        background-color: black;
        opacity: 0.6;
        transition: opacity 0.2s;
    }

    .card:hover .darken {
        opacity: 0.35;
        transition: opacity 0.2s;
    }

    .card-title {
        color: white;
        position: absolute;
        bottom: 0;
        display: block;
    }
</style>
