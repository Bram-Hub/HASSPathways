import Vue from 'vue'
import Router from 'vue-router'

import PathwaysPage from '../pages/Pathway/PathwaysPage.vue'
import PathwayPage from '../pages/Pathway/PathwayPage.vue'
import MyPathwaysPage from '../pages/MyPathways/MyPathwaysPage.vue'
import APathwayPage from '../pages/MyPathways/APathwayPage.vue'
import Four0FourPage from '../pages/Four0FourPage.vue'

import { pathways } from '../data/data.js'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: PathwaysPage,
        },
        {
            path: '/pathways',
            name: 'home',
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
            path: '/a-pathway',
            name: 'a-pathway',
            component: APathwayPage
        },
        {
            path: '*',
            name: '',
            component: Four0FourPage,
        },
    ],
    mode: 'history',
})
