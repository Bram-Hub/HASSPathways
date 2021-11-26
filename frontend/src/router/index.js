import Vue from 'vue'
import Router from 'vue-router'
import MyPathways from '../components/MyPathways/MyPathways.vue'
import ExpansionPanel from '../components/ExpansionPanel/ExpansionPanel.vue'

import HomePage from '../pages/Home/HomePage.vue'
import PathwayPage from '../pages/Pathway/PathwayPage.vue'
import MyPathwaysPage from '../pages/MyPathways/MyPathwaysPage.vue'
import APathwayPage from '../pages/MyPathways/APathwayPage.vue'

import { pathways } from '../data/data.js'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/home',
            name: 'home',
            component: ExpansionPanel,
        },
        {
            path: '/pathways',
            name: 'home',
            component: HomePage,
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
            path: '/test3',
            name: 'my-pathways',
            component: MyPathwaysPage
        },
        {
            path: '/test4',
            name: 'a-pathway',
            component: APathwayPage
        },
        {
            path: '/activity',
            name: 'activity',
            component: MyPathways,
        },
        {
            path: '*',
            name: '',
            component: ExpansionPanel,
        },
    ],
    mode: 'history',
})
