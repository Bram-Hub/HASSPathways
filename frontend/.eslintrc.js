module.exports = {
  env: {
    node: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/recommended',
    'plugin:prettier/recommended',
  ],
  rules: {
    'vue/this-in-template': 'off',
    'vue/no-unused-vars': 'error',
  },
}
