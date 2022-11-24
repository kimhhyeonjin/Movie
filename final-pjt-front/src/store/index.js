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
    recommendedMovies: [],
    popularityMovies: [],
    upcomingMovies: [],
    topRatedMovies: [],
    articles: [],
    article: [],
    comments: [],
    reviews: [],
    // token: null,로 하면 App.vue에서 v-if가 적용되지 않음
    // token: '',로 하면 적용됨
    isLogin: false,
    token: '',
    user: '',
    createUser: '',
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
    GET_RECOMMENDED_MOVIES(state, movies) {
      state.recommendedMovies = movies
    },
    GET_UPCOMING_MOVIES(state, movies) {
      state.upcomingMovies = movies
    },
    GET_TOP_RATED_MOVIES(state, movies) {
      state.topRatedMovies = movies
    },
    GET_POPULARITY_MOVIES(state, movies) {
      state.popularityMovies = movies
    },
    GET_ARTICLELIST(state, articles) {
      state.articles = articles
    },
    GET_ARTICLEDETAIL(state, article) {
      state.article = article
    },
    GET_COMMENTLIST(state, comments) {
      state.comments = comments
    },
    NO_COMMENTLIST(state) {
      state.comments = []
    },
    GET_REVIEWLIST(state, reviews) {
      state.reviews = reviews
    },
    NO_REVIEWLIST(state) {
      state.reviews = []
    },
    SIGNUP(state, token) {
      state.token = token
      router.push({ name: 'LoginView' })
    },
    LOGIN(state, token) {
      state.token = token
      state.isLogin = true
      router.push({ name: 'MovieView' })
    },
    LOGOUT_USER(state) {
      state.user = ''
      state.token = ''
      state.isLogin = false
      router.push({ name: 'LoginView' })
    },
    GET_USER(state, user) {
      state.user = user
    },
    GET_CREATE_USER(state, createUser) {
      state.createUser = createUser
    },
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
          context.commit('GET_MOVIES', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
    getRecommendedMovies(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/recommend/${payload}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((response) => {
          context.commit('GET_RECOMMENDED_MOVIES', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
    getUpcomingMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/upcoming/`,
      })
        .then((response) => {
          context.commit('GET_UPCOMING_MOVIES', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
    getTopRatedMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/top-rated/`,
      })
        .then((response) => {
          context.commit('GET_TOP_RATED_MOVIES', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
    getPopularMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/popularity/`,
      })
        .then((response) => {
          context.commit('GET_POPULARITY_MOVIES', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
    getArticleList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/communities/articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((response) => {
          context.commit('GET_ARTICLELIST', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
    getArticleDetail(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/communities/articles/${payload}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((response) => {
          context.commit('GET_ARTICLEDETAIL', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
    getCommentList(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/communities/articles/${payload}/comments/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((response) => {
          context.commit('GET_COMMENTLIST', response.data)
        })
        .catch(() => {
          // console.log(error)
          context.commit('NO_COMMENTLIST')
        })
    },
    getReviewList(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${payload}/reviews/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((response) => {
          context.commit('GET_REVIEWLIST', response.data)
        })
        .catch(() => {
          // console.log(error)
          context.commit('NO_REVIEWLIST')
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
          context.commit('SIGNUP', response.data.key)
        })
        .catch(() => {
          // console.log(error)
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
          context.commit('LOGIN', response.data.key)
          context.dispatch('getUser', response.data.key)
        })
        .catch(() => {
          // console.log(error)
          alert('다시 시도해주세요')
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
        .then(() => {
          context.commit('LOGOUT_USER')
        })
        .catch(() => {
          // console.log(error)
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
          context.commit('GET_USER', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
    getCreateUser(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/userdetail/${payload}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((response) => {
          context.commit('GET_CREATE_USER', response.data)
        })
        .catch(() => {
          // console.log(error)
        })
    },
  },
  modules: {
  }
})
