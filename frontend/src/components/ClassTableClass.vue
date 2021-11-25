<template>
    <v-card
        :class="[selectedClass(), 'w-100', 'my-2', 'class-card']"
        fluid
        outlined

        @click="toggleCheckbox()"
    >
        <v-list-item one-line>
            <v-list-item-content class="pb-0"> 
                <div style="cursor: pointer">
                    <h1 class="text-h5 class-card__title">
                        {{ clazz.name }}
                        <v-checkbox
                            :input-value="selected"
                            :false-value="0"
                            :true-value="1"

                            color="primary"
                            value="primary"
                            hide-details
                            class="d-inline-block ma-0 float-right"
                            style="z-index: 99"
                        />
                    </h1>

                    <small class="class-card__subtitle">
                        {{ clazz.prefix }}-{{ clazz.ID }}
                        <ClassTableModifiers
                            class="mt-4 class-card__subtitle__modifiers"
                            :item="clazz"
                        />
                        
                    </small>
                </div>
            </v-list-item-content>
        </v-list-item>
        <v-card-text class="class-card__desc">
            {{ clazz.description }}
        </v-card-text>
    </v-card>
</template>

<script>
import ClassTableModifiers from './ClassTableModifiers'

const requiredProps = ['name', 'prefix', 'ID', 'description', 'modifiers'];

export default {
    name: 'ClassTableClass',
    components: {
        ClassTableModifiers
    },
    props: {
        clazz: {
            type: Object,
            required: true,
            validator: clazz => requiredProps.every(prop => Object.keys(clazz).includes(prop))
        }
    },
    data: () => {
        return { selected: 0 }
    },
    methods: {
        toggleCheckbox() {
            let selection = window.getSelection();
            if (selection.isCollapsed)
                this.selected = 1 - this.selected;
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
