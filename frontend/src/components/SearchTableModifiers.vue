<template>
    <div style='justify: center;'>
        <v-tooltip top>
            <template #activator="{ on, attrs }">
                <v-chip
                    :color="myColor"
                    v-bind="attrs"
                    v-on="on"
                    @click="debugging()"
                >
                    {{ modifier }}
                </v-chip>
            </template>
            <span> {{myTooltip}} </span>
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

import { modifiers } from '../data/search-modifiers.js'

export default {
    name: 'SearchTableModifiers',
    props : {
        modifier: {
            type: String,
            required: true
        },
        course: {
            type: Object,
            required: true
        }
    },
    data: () => {
        return { 
            modifiers
        };
    },
    computed: {
        
        // This function should generate
        // an array of all modifiers
        myColor() {
            return this.course[this.modifier] ? this.modifiers[this.modifier]["color"] : 'dd4e47'
        },
        myTooltip() {
            return this.modifiers[this.modifier].tooltip
        }
    },
     methods: {
         debugging(){
             console.log("debugging")
             console.log(this.modifiers)
             
         }
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
