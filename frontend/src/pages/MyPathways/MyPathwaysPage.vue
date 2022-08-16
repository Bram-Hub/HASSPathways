<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <v-btn v-if="debugging" @click="debug()">
                debug
            </v-btn>
            <v-btn v-if="debugging" @click="debug2()">
                debug 2
            </v-btn>


            <h1>My HASS Pathways</h1>

            <p>
                Here you can find all your HASS pathways.
                <router-link to="/pathways">
                    You can add pathways here.
                </router-link>
            </p>
            <v-btn @click="bookmarkedOnly = !bookmarkedOnly">
                Toggle bookmarked pathways
            </v-btn>

            <v-divider class="my-4" />


            <MyPathway
                v-for="(item, index) in pathwaysToShow"
                :key="index"
                :title="item.name"
                :courses="item.courses"
                :pathway-category="item.name"
                :pre-requisite="item.preRequisite"
                :has-data="hasData"
                :can-delete="true"
                @update="update()"
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
        }
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.my_pathways,
            bookmarkedOnly: false,
            hasData: false,
            debugging: false,
        };
    },
    computed: {
        pathwaysToShow() {
            if (this.hasData) { /* this if statement is purposely empty */ }
            if ( this.bookmarkedOnly ) {
                return this.bookmarked;
            } else {
                return this.pathways;
            }
        },
        pathways() {
            if (this.hasData) { /* this if statement is purposely empty */ }
            let output = Object.entries(this.$store.state.pathways).map(v => { return {
                name: v[0],
                courses: v[1].courses,
                bookmarked: (v[1].bookmarked == true ? true : false),
            }});
            return output;
        },
        bookmarked() {
            if (this.hasData) { /* this if statement is purposely empty */ }
            let show = this.pathways.filter( pathway => pathway.bookmarked === true )
            return show;
        }
    },
    created() {
        this.hasData = true;
    },
    async mounted() {
        this.get_pathways().forEach(pathway => {
            if (pathway.courses.length == 0 && !pathway.bookmarked ) {
                this.$store.commit('delPathway', pathway.name);
                this.update();
            }
        })

    },
    methods: {
        debug2() {
            console.log("changing hasData")
            this.hasData = !this.hasData;
        },
        debug() {
            // add a test course
            console.log(this.pathways)
            console.log(this.bookmarked)
            let c = { "pathwayID": "Artificial Intelligence", "course": "Introduction to Cognitive Science" };
            this.$store.commit('addCourse', c);
            this.hasData = false;
            this.hasData = true;
            this.$forceUpdate();
        },
        get_pathways() {
            let output = Object.entries(this.$store.state.pathways).map(v => { return {
                name: v[0],
                courses: v[1].courses,
                bookmarked: (v[1].bookmarked == true ? true : false),
            }});
            return output 
        },
        update() {
            this.hasData = !this.hasData;
        },
    }
}
</script>
