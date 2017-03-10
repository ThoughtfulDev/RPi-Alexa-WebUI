import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login/Login'
import Dashboard from '../components/Dashboard/Dashboard'
import Logout from '../views/Logout'
import DetailCompanion from '../components/Details/CompanionService'
import DetailJavaClient from '../components/Details/JavaClient'
import DetailWWA from '../components/Details/WakeWordAgent'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  routes: [
    {
      path: '/',
      component: Login
    },
    {
      path: '/dashboard',
      component: Dashboard
    },
    {
      path: '/logout',
      component: Logout
    },
    {
      path: '/dashboard/details/companion',
      component: DetailCompanion
    },
    {
      path: '/dashboard/details/javaclient',
      component: DetailJavaClient
    },
    {
      path: '/dashboard/details/wakewordagent',
      component: DetailWWA
    }
  ]
})
