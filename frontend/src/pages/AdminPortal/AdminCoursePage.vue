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
                multiple
                label="Pathways"
                outlined
                chips
                readonly
            />
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
                    }
                }
            }
            this.pathways.push(singlePathway.name);
        }
        this.myPathways = Array.from(myPathways);
    },
    computed: {
        foundCrumbs() {
            const course = this.getCourse();
            if(course) {
                return breadcrumbs.pathway_template.map(x => x || {
                    text: course.name,
                    href: '/admin-portal/course?class=' + encodeURIComponent(course.name.slice().toLowerCase().replace(/ /g, '_'))
                });
            }
            else {
                return breadcrumbs.pathway_template.map(x => x || {
                    text: "Empty Course",
                    href: '/admin-portal/search-course-code'
                });
            }
        },
    },
    methods: {
        getCourse() {
            if(!this.$route.query.class) {
                return null;
            }
            return courses[this.$route.query.class];
        },
    }
}
</script>