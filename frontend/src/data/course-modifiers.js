import colors from 'vuetify/lib/util/colors'

export const modifiers = {
    'fall': {
        name: null,
        tooltip: 'Offered in the fall',
        icon: 'mdi-leaf-maple',
        color: 'red',
        search: ['fall', 'autumn']
    },
    'summer': {
        name: null,
        tooltip: 'Offered in the summer',
        icon: 'mdi-weather-sunset',
        color: 'orange',
        search: ['summer']
    },
    'spring': {
        name: null,
        tooltip: 'Offered in the spring',
        icon: 'mdi-flower',
        color: 'green',
        search: ['spring']
    },

    'CI': {
        name: 'CI',
        tooltip: 'Communication intensive',
        color: colors.blue.darken3,
        search: ['communication intensive', 'ci', 'com']
    },
    'DI': {
        name: 'DI',
        tooltip: 'Data intensive',
        color: colors.blue.darken3,
        search: ['data intensive', 'di', 'data']
    },
    'HI': {
        name: 'HI',
        tooltip: 'HASS inqury',
        color: colors.blue.darken3,
        search: ['hass inqury', 'hi', 'inqury', 'hass']
    },
    'major_restrictive': {
        name: 'MR',
        tooltip: 'Major restricted',
        color: colors.red.darken3,
        search: ['major', 'restrict']
    }
};

// Note: icon modifiers are ALWAYS sorted before textModifiers, regardless
// of the ordering below. If a key is missing from modifierOrder the modifier
// will not be rendered
export const modifierOrder = ['fall', 'spring', 'summer', 'CI', 'DI', 'HI', 'major_restrictive'];
export const iconModifiers = modifierOrder.filter(modifier => !modifiers[modifier].name);
export const textModifiers = modifierOrder.filter(modifier =>  modifiers[modifier].name);
