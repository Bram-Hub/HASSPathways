<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Courses</h1>
            <p> 
                Select a course to view details about it.
            </p>

            <v-divider class="my-4" />

            <div class="course-categories fade-in">
                <v-expansion-panels>
                    <CourseCategory
                        v-for="item in courseCategories"
                        :key="item.name"
                        :title="item.name"
                        :image="item.image"
                        :text="item.text"
                        :courses="item.courses"
                    />
                </v-expansion-panels>
            </div>
        </v-container>
    </div>
</template>

<script>
import CourseCategory from '../../components/CourseCategory'
import Breadcrumbs from '../../components/Breadcrumbs'
import { courseCategories } from '../../data/data.js'
import breadcrumbs from '../../data/breadcrumbs.js'

export default {
    components: { CourseCategory, Breadcrumbs },
    data: () => {
        return {
            courseCategories,
            breadcrumbs: breadcrumbs.courses,
        };
    },
}
</script>

<style scoped>

.search {
  float:right;
  position:relative;
}


.fade-in {
  animation: fadeIn 1s;
  -webkit-animation: fadeIn 1s;
  -moz-animation: fadeIn 1s;
  -o-animation: fadeIn 1s;
  -ms-animation: fadeIn 1s;
}

@keyframes fadein {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-webkit-keyframes fadein {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-moz-keyframes fadein {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-o-keyframes fadein {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-ms-keyframes fadein {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

.course-categories {
  max-width: 100vw;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  grid-gap: 10px;
}
</style>
