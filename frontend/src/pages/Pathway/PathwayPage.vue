<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            
            <h1>{{ pathway.name }}</h1>
            <p>{{ pathway.description }}</p>

            <div class="fab-container">
                <v-btn
                    color="green" elevation="2" fab
                    aria-label="Save pathway"
                >
                    <v-icon>mdi-content-save</v-icon>
                </v-btn>
            </div>

            <v-divider class="my-4" />

            <v-tabs
                v-model="tab"
                background-color="transparent"
                color="basil"
                grow
                center-active
            >
                <v-tabs-slider color="primary" />
                <v-tab
                    v-for="item in classTabs"
                    :key="item"
                >
                    <small>{{ item }}</small>
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab" touchless>    
                <v-tab-item
                    v-for="(item, index) in classTabs"
                    :key="item"
                    :eager="true"
                >
                    <ClassTable :classes="classes[index]" />
                </v-tab-item>
            </v-tabs-items>
        </v-container>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import { pathways, courses } from '../../data/data.js'

import ClassTable from '../../components/ClassTable'
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

const pathway = pathways[Object.keys(pathways)[4]];

function getClasses(classIds) {
    let r = classIds
        .map(clazz => courses[clazz])
        .filter(c => c.offered.fall || c.offered.spring || c.offered.summer);
    r.forEach(c => c.modifiers = ['fall', 'spring', 'summer', 'CI', 'DI', 'HI', 'major_restrictive'].filter(
        p => c.offered[p] || c.properties[p]
    ))
    return r;
}

const priorities = [pathway.priority1, pathway.priority2, pathway.priority3, pathway.priority4];

console.log(pathway)

export default {
    components: {
        ClassTable, Breadcrumbs
    },
    props: {
        classTabs: {
            type: Array,

            // TODO: only considered AFTER classes have been filtered
            default: () => [
                '1st Course',
                '2nd Course',
                '4000 Level',
                'Minor (optional)'
            ].filter((_, index) => priorities[index] && priorities[index].length)
        }
    },
    data() {
        return {
            tab: null,
            category: '',
            classes: priorities.map(getClasses),
            pathway: pathway,
            breadcrumbs: breadcrumbs.pathway_template.map(x => x || {
                text: pathway.name,
                href: '/'
            })
        }
    },
    methods: {
        ...mapMutations([
            'setSelectedCourse1',
            'setSelectedCourse2',
            'setSelectedCourse3',
            'setSelectedPathway',
        ]),
        findAllCourses(path) {
            var courses = []
            for (var x = 0; x < path.priority1.length; x++) {
                courses.push(this.findCourse(path.priority1[x]))
            }
            return courses
        },
        selectCourse(course, path) {
            this.setSelectedPathway(path.name)
            this.setSelectedCourse1(course)
            if (this.$store.editingCourses) {
                this.setSelectedCourse2(null)
                this.setSelectedCourse3(null)
            }
            console.log(course)
            this.$emit('nextBucket', this.nextBucketNumber)
            this.$root.$emit('makeSecondCourseEditable', true)
            this.$root.$emit('changeCurrent', 2)
            this.$root.$emit(`closePanels`)
        },
        findCourse(course) {
            var courses = this.allCourses
            for (var courseKey in courses) {
                if (course == courses[courseKey].pk) {
                    return courses[courseKey]
                }
            }
        },
    },
}
</script>

<style scoped>
.fab-container {
    position: fixed;
    right: 10px;
    bottom: 10px;
    width: 56px;
    height: 56px;
    z-index: 999;
    
    display: flex;
    justify-content: space-between;
}

@media only screen and (min-width: 600px) {
    .fab-container {
        right: 50px;
        bottom: 50px;
    }
}
</style>
