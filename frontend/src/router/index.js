import Vue from 'vue'
import Router from 'vue-router'
import MyPathways from '../components/MyPathways/MyPathways.vue'
import ExpansionPanel from '../components/ExpansionPanel/ExpansionPanel.vue'

import HomePage from '../pages/Home/HomePage.vue'
import PathwayPage from '../pages/Pathway/PathwayPage.vue'
import MyPathwaysPage from '../pages/MyPathways/MyPathwaysPage.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/home',
            name: 'home',
            component: ExpansionPanel,
        },
        {
            path: '/test',
            name: 'home',
            component: HomePage,
        },
        {
            path: '/test2',
            name: 'pathway',
            component: PathwayPage,
        },
        {
            path: '/test3',
            name: 'my-pathways',
            component: MyPathwaysPage
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
