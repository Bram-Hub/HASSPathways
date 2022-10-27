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
            <v-btn @click="all()">
                open all
            </v-btn>
			{{ panel }}
            <v-btn @click="none()">
                close all
            </v-btn>
            <h3>Professors:</h3>
            <ul>
                <li v-for="(prof, index) in course.professors" :key="prof">
                    {{ prof }}
                    <v-expansion-panels v-model="panel[index]" multiple>
                        <v-expansion-panel v-for="sec in profSec[prof]" :key="sec">
                            <v-expansion-panel-header>Section information</v-expansion-panel-header>
                            <v-expansion-panel-content>
                                Days: {{ course.sections['' + sec].days }} <br>
                                Time: {{ course.sections['' + sec].time }} <br>
                                Location: {{ course.sections['' + sec].location }} <br>
                                Type: {{ course.sections['' + sec].type }} <br><br>
                            </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-expansion-panels>
                </li>
            </ul>
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
            coursesData: {},
            panel: [] 
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
        profSec(){
            let profSec = {};
            for (let i = 0; i < this.course.professors.length; i++) {
                let prof = this.course.professors[i];
                let sec = [];
                for (var section in this.course.sections) {
                    if (this.course.sections[section]["instructor"] === prof){
                        sec.push(section);
                    }
                }
                profSec[prof] = sec;
            }
            return profSec;
        },
        numSections() {
            return this.course.sections.length;
        },
    },
    created() {
        const year = this.$store.state.year;
        import('../../data/json/' + year + '/courses.json').then((val) => {
            this.coursesData = Object.freeze(val);
            let courseID = this.$route.query.course;
            if (!Object.keys(this.coursesData).includes(courseID)) {
                this.$router.push('/404');
            }
        });
    },
    methods: {
        all() {
            let tempPanel = []
            for (var prof in this.course.professors) {
                tempPanel.push([...Array(this.profSec[this.course.professors[prof]].length).keys()].map((k,i) => i));
            }
            this.panel = tempPanel;
        },
        none() {
            this.panel = []
        },
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
