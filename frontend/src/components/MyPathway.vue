<template>
    <v-card
        class="rounded-0 card"
        elevation="1"
        :style="{ borderColor: colorHash(title) }"
    >
        <v-card-title class="font-weight-bold text-truncate card-title title-container">
            <span class="title-text text-truncate">
                {{ title }}
            </span>

            <v-menu bottom right>
                <template #activator="{ on, attrs }">
                    <v-btn
                        icon
                        v-bind="attrs"
                        v-on="on"
                    >
                        <v-icon>mdi-dots-vertical</v-icon>
                    </v-btn>
                </template>

                <v-list dense>
                    <v-list-item
                        v-for="(item, i) in menuItems"
                        :key="i"
                        link
                        @click="listAction(item.action)"
                    >
                        <v-list-item-icon class="mr-3">
                            <v-icon :color="item.color" dense v-text="item.icon" />
                        </v-list-item-icon>
                        <v-list-item-title>
                            {{ item.title }}
                        </v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-card-title>
        
        <div class="courses-container">
            <div class="course-items-container">
                <span
                    v-for="(course, i) in formatCourseCategory(courses)"
                    :key="i"
                >
                    <p class="pa-0 mb-2">
                        {{ course.name }}<br>
                        <small v-if="course.hasData" style="opacity: 0.8">{{ course.subj }}-{{ course.ID }}</small>
                        <small v-if="!course.hasData" style="opacity: 0.8">
                            No data available
                        </small>
                    </p>
                </span>
            </div>
        </div>
    </v-card>
</template>

<script>
import getColorFromCategry from '../helpers/category-colors.js';
import { pathwayCategories, courses as allCourses } from '../data/data.js'

export default {
    name: 'MyPathway',
    props: {
        title: {
            type: String,
            required: true
        },
        courses: {
            type: Array,
            required: true
        },
        pathwayCategory: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            menuItems: [
                { title: 'Edit Pathway', icon: 'mdi-pencil', action: 'edit' },
                { title: 'Graph View', icon: 'mdi-graph', action: 'graph' },
                { title: 'Delete Pathway', icon: 'mdi-delete', color: 'red', action: 'delete' },
            ],
        }
    },
    methods: {
        formatCourseCategory(classes) {
            if (!classes || !classes.length)
                return []; // Shouldn't happen!
            let out = [];
            for(const clazz in classes) {
                if(allCourses[classes[clazz]]) {
                    let myClass = allCourses[classes[clazz]];
                    myClass.hasData = true;
                    out.push(myClass);
                }
                else {
                    out.push({
                        name: classes[clazz],
                        hasData: false
                    })
                }
            }

            return out;
        },
        colorHash(pathway) {
            let category = pathwayCategories.filter(x => x.pathways.includes(pathway))[0];
            return getColorFromCategry(category ? category.name : '');
        },
        listAction(action) {
            if(action == 'edit') {
                let url ="/pathway?pathway=";
                url += encodeURIComponent(this.title);
                this.$router.replace(url);
            }
            else if(action == "delete") {
                this.$store.commit('delPathway', this.title);
                this.$emit('update');
            }
        }
    }
}
</script>

<style scoped lang="scss">
.card {
    margin: 5px;
    width: 340px;
    height: 450px;

    max-width: 95%;
    max-height: 90%;

    display: inline-flex;
    flex-direction: column;
    vertical-align: top;
    border-top: 3px solid var(--v-primary-base);

    .title-container {
        display: flex;
        flex-wrap: nowrap;
        justify-content: space-between;
        padding: 12px 16px;

        .title-text {
            padding-right: 20px;
            display: inline-block;
            width: 100%;
            font-size: 14pt;
        }

        .menu-icon {
            margin: 0 8px;
            float: right;
        }
    }

    .subheader {
        // Make divider subheader smaller and no inset
        height: 24px;
        padding-left: 0;
        font-size: 9pt;
        text-transform: uppercase;
    }

    .courses-container {
        padding: 0 20px;
        overflow-y: auto;
        background-color: rgba(0, 0, 0, 0.1); // TODO: padding for title, make theme dependent
        height: 100%;
        
        .course-items-container {
            padding-top: 12px;
            margin-bottom: 12px;
        }
    }
}
</style>
