# frontend

## Project setup
```
npm install
```
### Compiles and hot-reloads for development
```
npm run serve
```
### Compiles and minifies for production
```
npm run build
```
### Lints and fixes files
```
npm run lint
```
### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Project Layout
``src`` contains the frontend code
  |
  ----``assets`` contains image assets needed for frontend
  |      |
  |      ----``pathway-groups`` contains images for each pathway group
  |
  ----``components`` contains all Vue components
  |
  ----``data`` contains files used to manipulate and store data.
  |      |
  |      ----``json`` contains all json files that contain the data for the site
  |
  ----``helpers`` contains helper javascript files used within frontend
  |
  ----``pages`` contains all Vue Pages.
  |
  ----``router`` contains javascript file that defines the routing of pages.
  |
  ----``store`` contains the a javascript file that defines the Vuex store.
  |
  ----``sytles`` contains global stylesheet

## Frontend Tool
The frontend is made primarily using Vue and the [Vuetify](vuetifyjs.com/) library. To get started on a specific issue it is recommended to download [Vue devtools](https://devtools.vuejs.org/). 