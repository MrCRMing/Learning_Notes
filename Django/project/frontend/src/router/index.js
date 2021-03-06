import Vue from 'vue'
import Router from 'vue-router'

import Home from '../views/Home'
import CuteCat from '../views/CuteCat'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/cutecate/:cat_id',
      name: 'cutecat',
      component: CuteCat
    }
  ],
  mode: 'history'
})
