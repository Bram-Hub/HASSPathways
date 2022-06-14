<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />

            <h1>My HASS Pathways</h1>

            <p>
                Here you can find all your HASS pathways.
                <router-link to="/pathways">
                    You can add pathways here.
                </router-link>
            </p>

            <v-divider class="my-4" />


            <MyPathway
                v-for="(item, index) in get_pathways()"
                :key="index"
                :title="item.name"
                :courses="item.courses"
                :pathway-category="item.name"
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
            breadcrumbs: breadcrumbs.my_pathways
        };
    },
    async mounted() {
        this.get_pathways().forEach(pathway => {
            if (pathway.courses.length == 0) {
                this.$store.commit('delPathway', pathway.name);
                this.update();
            }
        })
    },
    methods: {
        get_pathways() {
            let output = Object.entries(this.$store.state.pathways).map(v => { return {
                name: v[0],
                courses: v[1].courses
            }});
            return output 
        },
        update() {
            this.$forceUpdate();
        }
    }
}
</script>
