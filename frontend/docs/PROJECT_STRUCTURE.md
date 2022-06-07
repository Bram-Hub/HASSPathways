# Project Structure

Up to date as of commit `1e407fb339af4c0df4d661561a6648757d3b61ac`

```
|- docs       - Documentation
|- public     - Favicons and other assets
|- src
    |- assets     - Images and other assets (TODO: figure out why this is duplicated)
    |- components - Put all Vue components here (see naming below)
        |- Unused files from old project
            - event-bus.js
    |- data       - JSONs and other "magic" constants / data
        |- json
            - courses.json            - "course_id" : { course data }
            - pathway_categories.json - [{ pathway_category }, ...]
            - pathways.json           - "pathway_id": { pathway data }
        - breadcrumbs.json      - Page breadcrumbs
        - course-modifiers.json - All course modifiers like "summer", "communication intensive", etc...
        - data.js               - Reads and formats/filters & exports the JSON data in ./json
        - vuex.js               - Vuex key constants
    |- helpers    - Util functions
        - category-colors.js    - Pathway category -> color hash function
        - search-courses.js     - Course search for a pathway page
    |- mixins     - Vue mixins (currently no mixins)
    |- pages      - Every individual page component
    |- plugins
        - vuetify.js   - Config for the Vuetify plugin (adds material design components/styles)
    |- router      - URL -> page handling
        - index.js
    |- styles          - Any SCSS/CSS files. It's recommended to put CSS for components in the same file as the component, so this is usually reserved for global styles
        - _globals.scss
    
```


## Naming
- Components should have their parent's name in title case, ie a row of a `Table` would be `TableRow`, not just `Row`

## Stuff for those unfamiliar with Vue / Node

### Top level files
- **.eslintrc.js** - Contains settings for the linter. If you have an eslint extension, it will use this and automatically highlight style errors.
- **.gitignore** - List of file/folder patterns to NOT add to git. For example, you probably don't want to upload the entire node_modules folder to git, so that goes here.
- **.prettierrc.js** - Config for a plugin for eslint that can automatically reformat improperly formatted code.
- **babel.config.js** - Used by Vue to "translate" modern JS into older JS for older browsers
- **package-lock.json** - Saves package versions / module list changes
- **package.json** - Contains project metadata, dependencies and some other stuff
- **README.md** - README file, contains project overview
- **vue.config.js** - Vue config
- **webpack.config.js** - Webpack config, currently used to compile SCSS files.

