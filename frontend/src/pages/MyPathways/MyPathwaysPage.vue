<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <!-- <v-btn @click="debug()">click me</v-btn> -->

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
        };
    },
    computed: {
        pathwaysToShow() {
            if ( this.bookmarkedOnly ) {
                return this.bookmarked;
            } else {
                return this.pathways;
            }
        },
        pathways() {
            let output = Object.entries(this.$store.state.pathways).map(v => { return {
                name: v[0],
                courses: v[1].courses,
                bookmarked: (v[1].bookmarked == true ? true : false),
            }});
            return output;
        },
        bookmarked() {
            let show = this.pathways.filter( pathway => pathway.bookmarked === true )
            return show;
        }
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
        debug() {
            console.log(this.pathways)
            console.log(this.bookmarked)
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
            this.$forceUpdate();
        },
    }
}
</script>
