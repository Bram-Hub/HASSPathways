<template>
    <v-card class="card" elecation="1">
        <v-img
            height="76px"
            class="card-img"
        >
            <!-- :src="require('../assets/course-groups/' + image)" -->
            <div class="darken" />

            <v-card-title class="font-weight-bold text-truncate card-title">
                {{ title }}
            </v-card-title>
        </v-img>

        <ul class="course-container">
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
    </v-card>
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

.card {
    width: 100%;
    max-width: calc(100vw - 24px);
	display: inline-block;
	vertical-align: top;
}

.darken {
    width: 100%;
	height: 100%;
    background-color: DarkSlateGray;
    opacity: 0.4;
	transition: opacity 0.2s;
}

.card:hover .darken {
    opacity: 0.1;
    transition: opacity 0.2s;
}

.card-title {
    color: white;
    position: absolute;
    bottom: 0;
    display: block;
    width: 100%;
}

.courses-container {
    overflow-y: auto;
    margin: 10px 0;
    list-style-type: square;
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
