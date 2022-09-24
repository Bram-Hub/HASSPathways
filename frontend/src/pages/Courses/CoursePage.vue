<template>
    <div style="width: 75%; margin: 0 auto;">
        <v-container fluid>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>
                Template Course Page
            </h1>
            <p> 
                I'm really just trying to get a feel for this format right now. 
            </p>
            <v-divider class="my-4" />
            <div class="btn-container">
                <div class="homepage-btn">
                    <v-btn
                        x-large
                        block
                        color="primary"
                        :to="{ name: 'pathways' }"
                    >
                        <v-icon left dark>
                            mdi-compass
                        </v-icon>
                        Explore pathways
                    </v-btn>
                </div>
            </div>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            year: '2022-2023',
        }
    },
    computed: {
        courseID() {
            // let courseID = this.$route.query.course;
            return 'art_history';
        },
        course() {
            if(!this.years[this.year][this.courseID]) {
                return {};
            }
            return this.years[this.year][this.courseID];
        },
        breadcrumbs() {
            return breadcrumbs.course_template.map(x => x || {
                text: 'Art History', 
                href: 'course?course=' + encodeURIComponent(this.courseID)
            })
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
