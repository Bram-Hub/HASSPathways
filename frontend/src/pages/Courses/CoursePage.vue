@ -1,101 +0,0 @@
<template>
    <v-container v-if="course.name">
        <Breadcrumbs :breadcrumbs="breadcrumbs" />
        <div class="header">
            <h1>{{ course.subj }}-{{ course.ID }}: {{ course.name }}</h1>
        </div>
        <p>{{ course.description }}</p>
        <h3>Instructor(s) name:</h3>
        <h4>Rate my Professor link:</h4>
        
        <template v-if="course.professors.length !== 0">
            <h3>Professors:</h3>
            <ul>
                <li v-for="pro in course.professors" :key="pro.id">
                    {{ pro }}
                    <template>
                        <h5>Section information:</h5>
                        <ul>
                            <li v-for="sec in course.sections" :key="sec.id">
                                    <h5>Section ID: {{ sec.id }}</h5>
                                    <h5>Section Type: {{ sec.type }}</h5>
                                    <h5>Section Time: {{ sec.time }}</h5>
                                    <h5>Section Location: {{ sec.location }}</h5>
                                    <h5>Section Days: {{ sec.days }}</h5>
                                    <h5>Section Instructor: {{ sec.instructor }}</h5>
                            </li>
                        </ul>
                    </template>
                </li>
            </ul>
            <h3> </h3>
        </template>
        <template v-else>
            <h3>This class is not providing in the current semester</h3>
        </template>
        <CourseTableModifiers
            class="mt-4 class-card__subtitle__modifiers"
            :item="course"
        />
        <v-divider class="my-4" />
    </v-container>
</template>

<script>
import { courseCategories } from '../../data/data.js'
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'
import CourseTableModifiers from '../../components/CourseTableModifiers'


export default {
    components: {
        Breadcrumbs,
        CourseTableModifiers
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
        },

        // Correspond Professors and their own section(s)
        profSec() {
            let profSec = [];
            for (let i = 0; i < this.course.professors.length(); ++i){
                let sec = [];
                let prof = this.course.professors[i];
                for (let j = 0; j < this.course.sections.length(); ++j)
                {
                    if (this.course.sections[j].instructor === prof){
                        sec.push(this.course.sections[j]);
                    }
                }
                profSec.push({professor: prof, sections: sec});
            }
            return profSec;
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