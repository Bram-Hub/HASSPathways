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
                    :class="[!item.modifiers.includes(modifier) ? 'inactive' : '' , 'modifier', 'modifier-icon']"
                    v-bind="attrs"
                    v-on="on"
                >
                    {{ modifiers[modifier].icon }}
                </v-icon>
            </template>
            <span>{{ modifiers[modifier].tooltip }}</span>
        </v-tooltip>
    
        <!-- Divider -->
        <v-divider vertical class="mx-2" />

        <!-- Text based modifiers, require a .name property -->
        <v-tooltip
            v-for="modifier in textModifiers"
            :key="modifier"
            top
        >
            <template #activator="{ on, attrs }">
                <v-chip
                    :class="[!item.modifiers.includes(modifier) ? 'inactive' : '' , 'modifier', 'modifier-text']"
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

// Existing modifiers
const modifiers = {
    'fall': {
        name: null,
        tooltip: 'Offered in the fall',
        icon: 'mdi-leaf-maple',
        color: 'red'
    },
    'summer': {
        name: null,
        tooltip: 'Offered in the summer',
        icon: 'mdi-weather-sunset',
        color: 'orange'
    },
    'spring': {
        name: null,
        tooltip: 'Offered in the spring',
        icon: 'mdi-flower',
        color: 'green'
    },

    'CI': {
        name: 'CI',
        tooltip: 'Communication intensive',
        color: 'blue'
    },
    'DI': {
        name: 'DI',
        tooltip: 'Data intensive',
        color: 'blue'
    },
    'HI': {
        name: 'HI',
        tooltip: 'HASS inqury',
        color: 'blue'
    },
    'major_restrictive': {
        name: 'MR',
        tooltip: 'Major restricted',
        color: 'red'
    }
};

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
        
        // Note: icon modifiers are ALWAYS sorted before textModifiers, regardless
        // of the ordering below. If a key is missing from modifierOrder the modifier
        // will not be rendered

        // TODO: move to modifiers list
        const modifierOrder = ['fall', 'spring', 'summer', 'CI', 'DI', 'HI', 'major_restrictive'];
        const iconModifiers = modifierOrder.filter(modifier => !modifiers[modifier].name);
        const textModifiers = modifierOrder.filter(modifier =>  modifiers[modifier].name);

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

    &.inactive {
        opacity: 0.5;
        // display: none;
    }
}

// Text-based modifiers
.modifier-text {
    padding: 0 !important;
    border-radius: 10px !important;
    width: 2em;
    height: 1.8em;
    
    display: inline-flex;
    justify-content: center;

    // Override default light/dark text colors when active
    &:not(.inactive) {
        color: #eee;
    }
}

// Inactive theme colors
.modifier.theme--light.inactive {
    &.modifier-text {
        background-color: #ccc !important;
    }
    &.modifier-icon {
        color: #bbb !important;
    }
}

.modifier.theme--dark.inactive {
    &.modifier-text {
        background-color: #333 !important;
    }
    &.modifier-icon {
        color: #666 !important;
    }
}
</style>
