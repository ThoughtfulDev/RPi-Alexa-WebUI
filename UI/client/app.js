import Vue from 'vue'
import Element from 'element-ui'
import { sync } from 'vuex-router-sync'
import App from './components/App'
import router from './router'
import store from './store'
sync(store, router)

const app = new Vue({
  router,
  store,
  ...App
})

Vue.use(Element)

export { app, router, store }
