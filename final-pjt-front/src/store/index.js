import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    // token: null,로 하면 App.vue에서 v-if가 적용되지 않음
    // token: '',로 하면 적용됨
    token: '',
    user: '',
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'MovieView' })
    },
    GET_USER(state, user) {
      state.user = user
      console.log(state.user)
    },
    LOGOUT_USER(state) {
      state.user = ''
      state.token = ''
      console.log(state.user)
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((response) => {
          // console.log(response)
          context.commit('GET_MOVIES', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((response) => {
          // console.log(response)
          context.commit('SAVE_TOKEN', response.data.key)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((response) => {
          console.log(response)
          context.commit('SAVE_TOKEN', response.data.key)
          context.dispatch('getUser', response.data.key)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getUser(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${payload}`
        },
      })
      .then((response) => {
        console.log(response)
        context.commit('GET_USER', response.data)
      })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          context.commit('LOGOUT_USER')
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  modules: {
  }
})
