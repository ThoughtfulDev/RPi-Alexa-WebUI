import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import config from '../config.js'
var jsstore = require('store')

Vue.use(Vuex)

const state = {
  session: jsstore.get('user_session'),
  isLoggedIn: checkLogin(),
  jsstore: jsstore,
  axios: axios.create({
    baseURL: config['API']
  })
}

function checkLogin () {
  var bcrypt = require('bcryptjs')
  const str = config['SECRET'] + config['HASHSECRET']
  if (jsstore.get('user_session') === undefined) {
    return false
  }
  return bcrypt.compareSync(str, jsstore.get('user_session').hash)
}

const mutations = {
  LOGOUT (state) {
    state.jsstore.remove('user_session')
    state.session = jsstore.get('user_session')
    state.isLoggedIn = checkLogin()
  }
}

const actions = {
  fetchSession ({ commit }) {
    state.session = jsstore.get('user_session')
    state.isLoggedIn = checkLogin()
  }
}

const store = new Vuex.Store({
  state,
  mutations,
  actions
})

export default store
