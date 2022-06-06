<template>
    <v-card
        :class="[selectedClass(), 'w-100', 'my-2', 'class-card']"
        fluid
        outlined

        @click="toggleCheckbox()"
        @keydown.13="toggleCheckbox()"
    >
        <v-list-item one-line>
            <v-list-item-content class="pb-0"> 
                <div style="cursor: pointer">
                    <h1 class="text-h5 class-card__title">
                        {{ course.name }}
                        <v-checkbox
                            :input-value="selected"
                            :false-value="0"
                            :true-value="1"

                            :aria-label="`Toggle selection for ${course.name}`"

                            color="primary"
                            value="primary"
                            hide-details
                            class="d-inline-block ma-0 float-right"
                            style="z-index: 99"
                        />
                    </h1>

                    <small class="class-card__subtitle">
                        {{ course.prefix }}-{{ course.ID }}
                        <CourseTableModifiers
                            class="mt-4 class-card__subtitle__modifiers"
                            :item="course"
                        />
                        
                    </small>
                </div>
            </v-list-item-content>
        </v-list-item>
        <v-card-text v-if="showDesc==true" class="class-card__desc" >
            {{ course.description }}
        </v-card-text>
    </v-card>
</template>

<script>
import CourseTableModifiers from './CourseTableModifiers'

const requiredProps = ['name', 'prefix', 'ID', 'description', 'modifiers'];

export default {
    name: 'CourseTableCourse',
    components: {
        CourseTableModifiers
    },
    props: {
        course: {
            type: Object,
            required: true,
            validator: course => requiredProps.every(prop => Object.keys(course).includes(prop))
        },
        pathwayId: {
            type: String,
            required: false,
            default: null
        },
        showDesc: {
            type:Boolean,
            required: false,
        }
    },
    data: () => {
        return { selected: 0 }
    },
    mounted() {
        // Load saved selection
        let courses = this.$store.state.pathways[this.pathwayId] || { courses: [] };
        courses = courses.courses;
        this.selected = courses.includes(this.course.key) ? 1 : 0;
    },
    methods: {
        toggleCheckbox() {
            let selection = window.getSelection();
            if (selection.isCollapsed) {
                this.selected = 1 - this.selected;

                // Save selection
                const c = { pathwayID: this.pathwayId, course: this.course.key };
                if (this.selected) this.$store.commit('addCourse', c);
                else               this.$store.commit('delCourse', c);
            }
        },
        selectedClass() {
            return this.selected ? 'class-card--selected' : '';
        },
        setSelected(selected) {
            // Convert truthy/falsy values -> 0/1 for vuetify checkbox
            selected = selected ? 1 : 0;
            this.selected = selected;
        }
    }
}
</script>

<style scoped lang="scss">
.class-card {
    max-width: 700px;
    border-radius: 0;

    &.class-card--selected {
        box-shadow: 0 0 0 1px var(--v-primary-base);
    }

    .class-card__title {
        line-height: 1.05em;
        display: inline-block;
        font-size: 1.2em !important;
        width: 100%
    }

    .class-card__subtitle {
        font-size: 0.9em;
        display: block;

        .class-card__subtitle__modifiers {
            transform: scale(0.75);
            transform-origin: bottom left;
            display: inline-block;

            position: relative;
            top: -5px;
            margin-left: 10px;
            margin-top: 0 !important
        }
    }

    .class-card__desc {
        padding: 8px 20px;
    }
}
</style>
