<template>
    <div>
        <!-- Non-text based modifiers go first (ie, the season icons) 
             The .name property should be null and a .icon property specified
             instead for a name in a <v-icon> -->
        <v-tooltip
            v-for="modifier in iconModifiers"
            :key="modifier"
            top
        >
            <template #activator="{ on, attrs }">
                <v-icon
                    :color="modifiers[modifier].color"
                    :class="[!item.modifiers.includes(modifier) ? 'modifier--inactive' : '' , 'modifier', 'modifier--icon']"
                    v-bind="attrs"
                    v-on="on"
                >
                    {{ modifiers[modifier].icon }}
                </v-icon>
            </template>
            <span>{{ modifiers[modifier].tooltip }}</span>
        </v-tooltip>
    
        <v-divider v-if="iconModifiers.length" vertical class="mx-2" />

        <!-- Text based modifiers, require a .name property -->
        <v-tooltip
            v-for="modifier in textModifiers"
            :key="modifier"
            top
        >
            <template #activator="{ on, attrs }">
                <v-chip
                    :class="[!item.modifiers.includes(modifier) ? 'modifier--inactive' : '' , 'modifier', 'modifier--text']"
                    :color="modifiers[modifier].color || 'primary'"
                    v-bind="attrs"
                    v-on="on"
                >
                    {{ modifiers[modifier].name }}
                </v-chip>
            </template>
            <span>{{ modifiers[modifier].tooltip }}</span>
        </v-tooltip>
    </div>
</template>

<script>
/**
 * Item is a class Object as defined in ClassTable.vue 
 * The modifiers property is an array of keys in the list
 * of modifiers in the data below, ie
 *   item.modifiers = [ 'HI',' fall', 'spring' ]
 *
 * The entire class object is passed for possible additional future formatting
 */

import { modifiers, modifierOrder, iconModifiers, textModifiers } from '../data/course-modifiers.js'

export default {
    name: 'ClassTableModifiers',
    props: {
        item: {
            type: Object,
            required: true,
            validator: item => item.modifiers.every(
                modifier => Object.keys(modifiers).includes(modifier))
        }
    },
    data: () => {
        console.assert(modifierOrder.every(k => Object.keys(modifiers).includes(k)),
            'modifierOrder contains modifiers that do not exist!');
        return { modifiers, modifierOrder, iconModifiers, textModifiers };
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
    }
    &.modifier--icon {
        color: #666 !important;
    }
}
</style>
