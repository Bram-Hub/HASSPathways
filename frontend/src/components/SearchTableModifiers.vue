<template>
    <div>
        <v-tooltip
            v-for="modifier in textModifiers"
            :class="[!myModifiers.includes(modifier) ? 'modifier--inactive' : '' , 'modifier', 'modifier--text']"
            :key="modifier"
            top
        >
            <template #activator="{ on, attrs }">
                <v-chip
                    :color="course[modifier] ? modifiers[modifier]['color'] : 'dd4e47'"
                    v-bind="attrs"
                    v-on="on"
                    @click="debugging()"
                >
                    {{ modifier }}
                </v-chip>
            </template>
            <span> {{modifiers[modifier].tooltip}} </span>
        </v-tooltip>
    </div>
</template>

<script>
/**
 * Item is a course Object as defined in CourseTable.vue 
 * The course object contains the offered and properties keys.
 *
 * The entire course object is passed for possible additional future formatting
 */

import { modifiers, iconModifiers, textModifiers } from '../data/search-modifiers.js'

export default {
    name: 'SearchTableModifiers',
    props : {
        course: {
            type: Object,
            required: true
        }
    },
    computed: {
        // This function should generate
        // an array of all modifiers
        myColor() {
            return this.course[this.modifier] ? this.modifiers[this.modifier]["color"] : 'dd4e47'
        },
        myTooltip() {
            return this.modifiers["Fall"].tooltip
            // return this.modifiers[this.modifier].tooltip
        },
        myModifiers() {
            let mods = [];
            for(const offer in this.course.offered) {
                if(this.course.offered[offer]) {
                    mods.push(offer);
                }
            }
            for(const prop in this.course.properties) {
                if(this.course.properties[prop]) {
                    mods.push(prop);
                }
            }

            return mods;
        }
    },
    data: () => {
        return { 
            modifiers,
            iconModifiers,
            textModifiers
        };
    }
}
</script>

<style scoped lang="scss">
// Base styles applied to all modifiers
.modifier {
    margin-right: 3px;
    cursor: help;
    user-select: none;
    overflow: visible;

    &.modifier--inactive {
        opacity: 0.5;
        display: none;
    }
}

// Text-based modifiers
.modifier--text {
    padding: 0 5px !important;
    border-radius: 10px !important;
    min-width: 2em;
    height: 1.8em;
    
    display: inline-flex;
    justify-content: center;

    // Override default light/dark text colors when active
    &:not(.modifier--inactive) {
        color: #eee;
    }
}

// Inactive theme colors
.modifier.theme--light.modifier--inactive {
    
    &.modifier--text {
        background-color: #ccc !important;
    }
    &.modifier--icon {
        color: #bbb !important;
        
    }
}

.modifier.theme--dark.modifier--inactive {
    &.modifier--text {
        background-color: #333 !important;
        display: inline-flex;
    }
    &.modifier--icon {
        color: #666 !important;
    }
}
</style>
