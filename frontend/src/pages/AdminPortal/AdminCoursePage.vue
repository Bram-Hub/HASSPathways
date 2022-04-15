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
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'
import { courses } from '../../data/data.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.admin_course_page,
            name: ""
        }
    },
    created() {
        this.name = this.getCourse().name;  
    },
    computed: {
        foundCrumbs() {
            let course = this.getCourse();
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