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
        <template>
        <v-expansion-panels>
            <v-expansion-panel
            v-for="(item,i) in 1"
            :key="i"
            >
            <v-expansion-panel-header>
                Sections
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                <button>  SectionNum-CRN | StartDate-EndDate </button> <br>
                <button>  SectionNum-CRN | StartDate-EndDate </button> <br>
                <button>  SectionNum-CRN | StartDate-EndDate </button> <br>
                <button>  SectionNum-CRN | StartDate-EndDate </button> <br>
            </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
        </template>
        <h3>Instructor(s) name:</h3>
        <h4>Rate my Professor link:</h4>
        <template>
        <v-expansion-panels>
            <v-expansion-panel
            v-for="(item,i) in 1"
            :key="i"
            >
            <v-expansion-panel-header>
                Sections
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                SectionNum-CRN | StartDate-EndDate 
            </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
        </template>
        <h3>Available: {{ course.offered.text }}</h3>
        <br>
        <h3>Prerequisites:</h3>
        <template v-if="course.prerequisites.length !== 0">
            <ul>
                <li v-for="prereq in course.prerequisites" :key="prereq.id">
                    {{ prereq }}
                </li>
            </ul>
        </template>
        <template v-else>
            <p>None</p>
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