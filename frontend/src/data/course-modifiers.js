import colors from 'vuetify/lib/util/colors'

export const modifiers = {
    'fall': {
        name: 'Fall',
        tooltip: 'Offered in the fall',
        icon: null, // 'mdi-leaf-maple',
        color: colors.red.darken3,
        search: ['fall', 'autumn']
    },
    'summer': {
        name: 'Summer',
        tooltip: 'Offered in the summer',
        icon: null, // 'mdi-weather-sunset',
        color: colors.orange.darken3,
        search: ['summer']
    },
    'spring': {
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
    },
    'pre_requisite': {
        name: 'PR',
        tooltip: 'This course has pre-requisite(s)',
        color: colors.red.accent3,
        search: ['prerequisite', 'pre-requisite', 'pre', 'requisite']
    }
};

// Note: icon modifiers are ALWAYS sorted before textModifiers, regardless
// of the ordering below. If a key is missing from modifierOrder the modifier
// will not be rendered
export const modifierOrder = ['fall', 'spring', 'summer', 'CI', 'DI', 'HI', 'major_restrictive', 'pre_requisite'];
export const iconModifiers = modifierOrder.filter(modifier => !modifiers[modifier].name);
export const textModifiers = modifierOrder.filter(modifier =>  modifiers[modifier].name);
