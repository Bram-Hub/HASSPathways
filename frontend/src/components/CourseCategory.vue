<template>
    <v-expansion-panel>
        <v-expansion-panel-header>
            {{ title }}
        </v-expansion-panel-header>
        <v-expansion-panel-content>
            <ul class="courses-container">
                <v-tooltip
                    v-for="course in filteredCourses"
                    :key="course"

                    bottom
                    eager
                    color="black"
                    offset-overflow
                    max-width="400px"
                    open-delay="700"
                    transition="none"
                >
                    <template #activator="{ on, attrs }">
                        <li class="course" v-bind="attrs" v-on="on">
                            <a :href="`/course?course=${encodeURIComponent(course)}`" class="text-decoration-none">
                                <b>{{ course }}</b>
                            </a>
                        </li>
                    </template>
                    <span v-if="coursesData[course]">{{ coursesData[course].description }}</span>
                </v-tooltip>
            </ul>
        </v-expansion-panel-content>
    </v-expansion-panel>
</template>

<script>

export default {
    name: 'CourseCategory',
    props: {
        title: {
            type: String,
            required: true
        },
        text: {
            type: String,
            default: '' 
        },
        image: {
            type: String,
            default: ''
        },
        courses: {
            type: Array,
            default: () => [],
        }
    },
    data() { return { coursesData: {} }; },
    computed: {
        filteredCourses() {
            let output = [];
            for(const course in this.courses) {
                if(this.coursesData[this.courses[course]]) {
                    output.push(this.courses[course]);
                }
            }
            return output;
        }
    },
    created() {
        const year = this.$store.state.year;
        import('../data/json/' + year + '/courses.json').then((val) => this.coursesData = Object.freeze(val));
    }
}
</script>


<style scoped lang="scss">

.courses-container {
	column-count: 3;
}

.course {
    padding: 6px 4px;
	margin-left: 8px;
	cursor: pointer;
	font-size: 0.875em;
}

.course:hover h4 {
    text-decoration: underline;
}

.course:last-child {
    border-bottom: none;
}
</style>
