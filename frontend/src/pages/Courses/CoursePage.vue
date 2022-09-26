<template>
    <v-container v-if="course.name">
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <div class="header">
            <h1>{{ course.subj }}-{{ course.ID }}: {{ course.name }}</h1>
        </div>
        <p>{{ course.description }}</p>
        <v-divider class="my-4" />
    </v-container>
</template>

<script>
import { courseCategories } from '../../data/data.js'
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            coursesData: {}
        }
    },
    computed: {
        // Get ID of course
        courseID() {
            let courseID = this.$route.query.course;
            return courseID;
        },
        // Get course object
        course() {
            if(!this.coursesData[this.courseID]) {
                return {};
            }
            return this.coursesData[this.courseID];
        },
        categoryName() {
            for (let category in courseCategories)
                if (category.courses.includes(this.courseID))
                    return category.name;
            return '';
        },
        breadcrumbs() {
            return breadcrumbs.course_template.map(x => x || {
                text: this.course.name, 
                href: 'course?course=' + encodeURIComponent(this.courseID)
            })
        }
    },
    created() {
        const year = this.$store.state.year;
        import('../../data/json/' + year + '/courses.json').then((val) => {this.coursesData = Object.freeze(val);
            let courseID = this.$route.query.course;
            if (!Object.keys(this.coursesData).includes(courseID)) {
                this.$router.push('/404');
            }
        });
    }
}
</script>

<style scoped>
 .homepage-btn {
     width: 350px;
     height: 50px;
 }
 .btn-container {
     padding: 10px 0;
     display: grid;
     justify-items: center;
     align-items: center;
     grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
     grid-gap: 10px;
     display: flex;
     flex-wrap: wrap;
     justify-content: center;
 }
</style>
