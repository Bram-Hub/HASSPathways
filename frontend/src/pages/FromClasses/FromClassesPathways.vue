<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Here are the pathways that match the selected courses!</h1>
            <h3>You can view the pathway further by clicking the 3 dots then edit pathway.</h3>
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
                let thisPathway = {name: "", courses: new Map()}; 
                const singlePathway = pathways[key];
                thisPathway.name = key;
                for(const prio in singlePathway) {
                    if(prio.substring(0, 8) == "priority") {
                        const courses = singlePathway[prio];
                        for(const i in courses) {
                            if(this.$store.state.classes[courses[i]]) {
                                let ID = this.$store.state.classes[courses[i]];
                                thisPathway.courses.set(courses[i], ID);
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
