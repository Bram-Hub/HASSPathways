<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />

            <h1>My HASS Pathways</h1>

            <p>Select a pathway below to get started, or <a>choose a pathway from the classes you've taken</a></p>

            <v-btn
                elevation="2"
            >
                Add from pathway
            </v-btn>
            <v-btn
                elevation="2"
            >
                Add from classes
            </v-btn>

            <v-divider class="my-4" />


            <MyPathway
                v-for="(item, index) in my_pathways"
                :key="index"
                :title="item.name"
                :classes="item.classes"
                :pathway-category="item.name"
            />
        </v-container>
    </div>
</template>

<script>
import MyPathway from '../../components/MyPathway'
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

export default {
    components: {
        MyPathway, Breadcrumbs
    },
    props: {
        path: {
            default: '',
            type: String,
        },
    },
    data() {
        const SAMPLE_CLASSES = {
            sec1: ['Made up class name', 'ARt history', 'more classes', 'even more'],
            sec2: [12345, 12345, 12345],
            sec3: [12345, 12345, 1233],
            minor: [123, 123, 123, 'long jkdjakdhadgasljsdhaskdsadaadadas'],
        };
        return {
            my_pathways: [{
                name: 'My pathway is a very long light novel title!',
                classes: SAMPLE_CLASSES
            },{
                name: 'Arts',
                classes: SAMPLE_CLASSES
            },{
                name: 'My pathway',
                classes: SAMPLE_CLASSES
            },{
                name: 'Fact and fiction',
                classes: SAMPLE_CLASSES
            }],
            breadcrumbs: breadcrumbs.my_pathways
        };
    }
}
</script>
