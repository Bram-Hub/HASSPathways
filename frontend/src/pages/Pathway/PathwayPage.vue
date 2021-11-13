<template>
    <div>
        <v-container>
            <h1>{{ pathway.fields.pathName }}</h1>
            <p>{{ pathway.fields.pathDescript }}</p>

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
import cJson from '../../../../JSONfiles/courses.json'
import pJson from '../../../../JSONfiles/pathways.json'

import ClassTable from '../../components/ClassTable'

const pathway = pJson[2];

function transformClass(clazz) {
    let modifiers = ['CI', 'DI', 'HI', 'fall', 'spring', 'summer', 'major_restrictive']
        .filter(modifier => clazz.fields[modifier]);
    return {
        name: clazz.fields.name,
        prefix: clazz.fields.prefix,
        id: clazz.fields.ID,
        description: clazz.fields.description,
        modifiers: modifiers,
        pk: clazz.pk
    };
}

export default {
    components: {
        ClassTable
    },
    props: {
        path: {
            default: () => pJson[0].fields
        },
        classTabs: {
            type: Array,
            default: () => [
                '1st Course',
                '2nd Course',
                '4000 Level',
                'Minor (optional)'
            ]
        }
    },
    data() {
        let filtered = cJson.filter(x => 
                pathway.fields.priority1.includes(x.pk) || pathway.fields.priority2.includes(x.pk) || pathway.fields.priority3.includes(x.pk))
                .filter(x => x.fields.summer || x.fields.fall || x.fields.spring)
                .map(transformClass);
        return {
            tab: null,
            category: '',
            classes: [
                filtered.filter(x => pathway.fields.priority1.includes(x.pk)),
                filtered.filter(x => pathway.fields.priority2.includes(x.pk)),
                filtered.filter(x => pathway.fields.priority3.includes(x.pk)),
                []
            ],
            pathway: pathway
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
            this.setSelectedPathway(path.pathName)
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
