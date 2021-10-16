module.exports = {
    env: {
        node: true,
    },
    extends: [
        'eslint:recommended',
        'plugin:vue/recommended',
        // 'plugin:prettier/recommended',
    ],
    rules: {
        'vue/this-in-template': 'off',
        'vue/valid-v-slot': ['off'],

        'no-unused-vars': 'warn',
        'vue/no-unused-vars': 'warn',

        'vue/html-indent': ['warn', 4],
        // 'prettier/tabSize': 4,
        'indent': ['warn', 4],

        'vue/max-attributes-per-line': ['warn', {
            'singleline': 4,
            'multiline': 4
        }]
    },
}
