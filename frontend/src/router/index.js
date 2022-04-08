import Vue from 'vue'
import Router from 'vue-router'

import HomePage from '../pages/HomePage.vue'
import PathwaysPage from '../pages/Pathway/PathwaysPage.vue'
import PathwayPage from '../pages/Pathway/PathwayPage.vue'
import MyPathwaysPage from '../pages/MyPathways/MyPathwaysPage.vue'
import FromClassesPage from '../pages/FromClasses/FromClassesPage.vue'
import FromClassesPathways from '../pages/FromClasses/FromClassesPathways.vue'
import Four0FourPage from '../pages/Four0FourPage.vue'

import { pathways } from '../data/data.js'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomePage,
        },
        {
            path: '/pathways',
            name: 'pathways',
            component: PathwaysPage,
        },
        {
            path: '/pathway',
            name: 'pathway',
            component: PathwayPage,
            beforeEnter: (to, from, next) => {
                next(!pathways[to.query.pathway] ? '/404' : undefined);
            }
        },
        {
            path: '/my-pathways',
            name: 'my-pathways',
            component: MyPathwaysPage
        },
        {
            path: '/search-classes',
            name: 'search-classes',
            component: FromClassesPage
        },
        {
            path: '/from-classes',
            name: 'from-classes',
            component: FromClassesPathways
        },
        {
            path: '*',
            name: '',
            component: Four0FourPage,
        },
    ],
    mode: 'history',
})
