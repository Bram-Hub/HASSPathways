import colors from 'vuetify/lib/util/colors'

export const modifiers = {
    'Fall': {
        name: 'Fall',
        tooltip: 'Offered in the fall',
        icon: null, // 'mdi-leaf-maple',
        color: colors.red.darken3,
        search: ['fall', 'autumn']
    },
    'Summer': {
        name: 'Summer',
        tooltip: 'Offered in the summer',
        icon: null, // 'mdi-weather-sunset',
        color: colors.orange.darken3,
        search: ['summer']
    },
    'Spring': {
        name: 'Spring',
        tooltip: 'Offered in the spring',
        icon: null, // 'mdi-flower',
        color: colors.green.darken3,
        search: ['spring']
    },
    'CI': {
        name: 'CI',
        tooltip: 'Communication intensive',
        color: colors.blue.darken3,
        search: ['communication intensive', 'ci', 'com']
    },
    'HI': {
        name: 'HI',
        tooltip: 'HASS inqury',
        color: colors.blue.darken3,
        search: ['hass inqury', 'hi', 'inqury', 'hass']
    }
};

// Note: icon modifiers are ALWAYS sorted before textModifiers, regardless
// of the ordering below. If a key is missing from modifierOrder the modifier
// will not be rendered
export const modifierOrder = ['Fall', 'Spring', 'Summer', 'CI', 'HI'];
export const iconModifiers = modifierOrder.filter(modifier => !modifiers[modifier].name);
export const textModifiers = modifierOrder.filter(modifier =>  modifiers[modifier].name);
