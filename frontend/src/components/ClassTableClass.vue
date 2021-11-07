<template>
    <v-card
        :class="[selectedClass(), 'w-100', 'my-2']"
        style="max-width: 700px"
        fluid
        outlined

        @click="toggleCheckbox()"
    >
        <v-list-item one-line>
            <v-list-item-content class="pb-0"> 
                <div
                    style="cursor: pointer"
                >
                    <h1 class="text-h5" style="line-height: 1.05em; display: inline-block; font-size: 1.2em !important; width: 100%">
                        {{ clazz.name }}
                        <v-checkbox
                            :input-value="selected"
                            :false-value="0"
                            :true-value="1"

                            color="primary"
                            value="primary"
                            hide-details
                            style="display: inline-block; margin: 0; z-index: 99; float:right"
                        />
                    </h1>

                    <small style="font-size: 0.9em; display: block;">
                        {{ clazz.prefix }}-{{ clazz.id }}
                        <ClassTableModifiers
                            class="mt-4"
                            style="transform: scale(0.75); transform-origin: bottom left; display: inline-block;
                        position: relative; top: -5px; margin-left: 10px; margin-top: 0 !important" :item="clazz"
                        />
                        
                    </small>
                </div>
            </v-list-item-content>
        </v-list-item>
        <v-card-text style="padding: 8px 20px;">
            {{ clazz.description }}
        </v-card-text>
    </v-card>
</template>

<script>
import ClassTableModifiers from './ClassTableModifiers'

const requiredProps = ['name', 'prefix', 'id', 'description', 'modifiers'];

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
        return {
            selected: 0
        }
    },
    methods: {
        toggleCheckbox() {
            let selection = window.getSelection();
            if (selection.toString().length === 0)
                this.selected = 1 - this.selected;
        },
        selectedClass() {
            return this.selected ? 'selected' : '';
        },
        setSelected(selected) {
            // Convert truthy/falsy values -> 0/1 for vueitfy checkbox
            selected = selected ? 1 : 0;
            this.selected = selected;
        }
    }
}
</script>

<style scoped lang="scss">
.selected {
    box-shadow: 0 0 0 1px var(--v-primary-base);
}
</style>
