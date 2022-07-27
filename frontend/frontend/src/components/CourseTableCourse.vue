<template>
    <v-card
        :class="[selectedClass(), 'w-100', 'my-2', 'class-card', {graph: graphView}]"
        fluid
        outlined
        @click="toggleCheckbox()"
        @keydown.13="toggleCheckbox()"
    >
        <v-list-item one-line>
            <v-list-item-content class="pb-0">
                <div style="cursor: pointer">
                    <h1 class="text-h5 class-card__title">
                        <v-checkbox
                            :input-value="selected"
                            :false-value="0"
                            :true-value="1"

                            :aria-label="`Toggle selection for ${course.name}`"

                            color="primary"
                            value="primary"
                            hide-details
                            class="d-inline-block ma-0 float-right checkbox"
                        />
                        {{ course.name }}
                    </h1>
                    <small v-if="course.hasData" class="class-card__subtitle">
                        {{ course.subj }}-{{ course.ID }}
                        <label v-for="el in course['cross listed']" :key="el">
                            / {{ el }}
                        </label>
                        <CourseTableModifiers
                            class="mt-4 class-card__subtitle__modifiers float-right"
                            :class="{graphChange:graphView}"
                            :item="course"
                        />

                    </small>
                </div>
            </v-list-item-content>
        </v-list-item>
        <v-card-text v-if="course.hasData && showDesc" class="class-card__desc">
            {{ course.description }}
        </v-card-text>
        <v-card-text v-if="!course.hasData" class="class-card__desc">
            Data not found within RPI catalog, see SIS for more info.
        </v-card-text>
    </v-card>
</template>

<script>
import CourseTableModifiers from './CourseTableModifiers'

const requiredProps = ['hasData', 'name'];

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
            type: Boolean,
            required: false,
        },
        descriptionOnHover: {
            type: Boolean,
            required: false,
            default: true,
        },
        graphView: {
            type: Boolean,
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
        this.selected = courses.includes(this.course.name) ? 1 : 0;
    },
    methods: {
        func(el) {
            console.log(el);
        },
        toggleCheckbox() {
            let selection = window.getSelection();
            if (selection.isCollapsed) {
                this.selected = 1 - this.selected;

                // Save selection
                const c = { pathwayID: this.pathwayId, course: this.course.name };
                if (this.selected){
                    this.$store.commit('addCourse', c);
                    this.$emit('checkbox-clicked')
                } else {
                    this.$store.commit('delCourse', c);
                }
            }
        },
        selectedClass() {
            return this.selected ? 'class-card--selected' : '';
        },
        setSelected(selected) {
            // Convert truthy/falsy values -> 0/1 for vuetify checkbox
            selected = selected ? 1 : 0;
            this.selected = selected;
        },
        isSelected() {
            return this.selected;
        }
    }
}
</script>

<style scoped lang="scss">
// .graph {
//     width: 50%;
// }
.v-tooltip__content {
  opacity: 2.0;
}
.checkbox {
    transform: scale(0.8);
    transform-origin: top-left;
 }
.class-card {
    /* max-width: 700px; */
    border-radius: 0;

    &.class-card--selected {
        box-shadow: 0 0 0 1px var(--v-primary-base);
    }

    .class-card__title {
        line-height: 1.05em;
        display: inline-block;
        font-size: 1.2em !important;
        width: 100%;
    }

    .class-card__subtitle {
        font-size: 0.9em;
        display: block;

        .class-card__subtitle__modifiers {
            transform: scale(0.90);
            transform-origin: top right;
            display: inline-block;

            position: relative;
            top: -5px;
            // margin-left: 10px;
            margin-top: 0 !important
        }
        .graphChange {
            display: block;
        }
    }

    .class-card__desc {
        padding: 8px 20px;
    }
}


</style>
