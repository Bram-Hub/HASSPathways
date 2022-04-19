<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="foundCrumbs" />
            <v-text-field
                v-model="name"
                outlined
                rounded
                label="Course Name"
            />
            <v-text-field
                v-model="dept"
                outlined
                rounded
                label="Department"
            />
            <v-text-field
                v-model="ID"
                outlined
                rounded
                label="Course ID"
                type="number"
            />
            <v-textarea
                v-model="description"
                outlined
                rounded
                label="Description"
            />
            <v-checkbox 
                v-model="CI"
                label="Communication Intensive"
            />
            <v-checkbox 
                v-model="HI"
                label="Hass Inquiry"
            />
            <v-checkbox 
                v-model="fall"
                label="Offered in Fall"
            />
            <v-checkbox 
                v-model="summer"
                label="Offered in Summer"
            />
            <v-checkbox 
                v-model="spring"
                label="Offered in Spring"
            />
            <v-select
                v-model="myPathways"
                :items="pathways"
                multiple
                label="Pathways"
                outlined
                chips
            />
            <v-btn color="primary" outlined @click="submit()">
                Submit Changes<v-icon>mdi-check</v-icon>
            </v-btn>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'
import { courses, pathways } from '../../data/data.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.admin_course_page,
            name: "",
            dept: "",
            ID: 0,
            CI: false,
            HI: false,
            description: "",
            fall: false,
            summer: false,
            spring: false,
            major_rest: false,
            minors: [],
            myPathways: [],
            pathways: []
        }
    },
    computed: {
        foundCrumbs() {
            const course = this.getCourse();
            console.log()
            if(course) {
                return breadcrumbs.admin_course_page.map(x => x || {
                    text: course.name,
                    href: '/admin-portal/course?class=' + encodeURIComponent(course.name.slice().toLowerCase().replace(/ /g, '_'))
                });
            }
            else {
                return breadcrumbs.admin_course_page.map(x => x || {
                    text: "Empty Course",
                    href: '/admin-portal/course'
                });
            }
        }
    },
    created() {
        const course = this.getCourse();
        if(course) {
            this.name = course.name;
            this.dept =  course.prefix;
            this.ID = course.ID;
            this.CI = course.properties.CI;
            this.HI = course.properties.HI;
            this.description = course.description;
            this.fall = course.offered.fall;
            this.summer = course.offered.summer;
            this.spring = course.offered.spring;
            this.major_rest = course.properties.major_restricted;
        }
        let myPathways = new Set();
        for(const key in pathways) {
            const singlePathway = pathways[key];
            if(course) {
                for(const prio in singlePathway) {
                    if(prio.substring(0, 8) == "priority") {
                        const array = singlePathway[prio];
                        if(array.includes(course.name.slice().toLowerCase().replace(/ /g, '_'))) {
                            myPathways.add(singlePathway.name);
                        }
                        this.pathways.push(singlePathway.name);
                    }
                }
            }
            this.pathways.push(singlePathway.name);
        }
        this.myPathways = Array.from(myPathways);
    },
    methods: {
        getCourse() {
            if(!this.$route.query.class) {
                return null;
            }
            return courses[this.$route.query.class];
        },
        submit() {
            let newCourse = this.getCourse();
            if(!newCourse) {
                newCourse = {
                    name: "",
                    prefix: "",
                    ID: 0,
                    properties: {
                        CI: 0,
                        HI: 0,
                        major_restricted: 0
                    },
                    description: "",
                    offered: {
                        fall: 0,
                        summer: 0,
                        spring: 0
                    },
                    key: ""
                };
            }
            newCourse.name = this.name;
            newCourse.prefix = this.dept;
            newCourse.ID = this.ID;
            newCourse.properties.CI = this.CI;
            newCourse.properties.HI = this.HI;
            newCourse.description = this.description;
            newCourse.offered.fall = this.fall;
            newCourse.offered.summer = this.summer;
            newCourse.offered.spring = this.spring;
            newCourse.properties.major_restricted = this.major_rest;
            newCourse.key = this.name.slice().toLowerCase().replace(/ /g, '_');
            console.log(newCourse);
            console.log(this.myPathways);
        }
    }
}
</script>