<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Matching Pathways</h1>
            <p>
                Here are the pathways that match the selected courses!
                You can view the pathway further by clicking the pencil icon,
                or <router-link :to="{ name: 'search-classes' }">
                    go back to picking courses.
                </router-link>
            </p>

            <v-divider class="my-4" />

            <div v-if="get_pathways.length === 0" style="text-align: center">
                <h1 class="text--disabled mb-4 mt-8 font-weight-light">
                    You haven't selected any courses :(
                </h1>
                <v-btn
                    tile
                    x-large
                    :to="{ name: 'search-classes' }"
                >
                    Go back
                </v-btn>
            </div>

            <MyPathway
                v-for="(item, index) in get_pathways"
                :key="index"
                :title="item.name"
                :courses="item.courses"
                :pathway-category="item.name"
            />
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import MyPathway from '../../components/MyPathway'
import breadcrumbs from '../../data/breadcrumbs.js'
import { pathways } from '../../data/data.js'

export default {
    components: {
        Breadcrumbs,
        MyPathway
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.from_classes_pathway,
            searchValue: ''
        }
    },
    computed: {
        get_pathways() {
            let myPathways = [];
            for(const key in pathways) {
                let thisPathway = {name: "", courses: new Set()};
                const singlePathway = pathways[key];
                thisPathway.name = key;
                for(const prio in singlePathway) {
                    //Checks if it has classes within it
                    if(singlePathway[prio] instanceof Object && !(singlePathway[prio] instanceof Array)) {
                        const courses = singlePathway[prio];
                        for(const name in courses) {
                            if(this.$store.state.classes[name]) {
                                thisPathway.courses.add(name);
                            }
                        }
                    }
                }
                if(thisPathway.courses.size > 0) {
                    thisPathway.courses = Array.from(thisPathway.courses.values());
                    myPathways.push(thisPathway);
                }
            }

            myPathways.sort((a, b) => a.courses.length < b.courses.length)
            return myPathways;
        }
    }
}
</script>
