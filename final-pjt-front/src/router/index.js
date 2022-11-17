import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import SearchView from '@/views/SearchView'
import RecommendView from '@/views/RecommendView'
import CommunityView from '@/views/CommunityView'
import MypageView from '@/views/MypageView'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import MovieDetail from '@/views/MovieDetail'
import ArticleDetail from '@/views/ArticleDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/mypage',
    name: 'MypageView',
    component: MypageView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/movie/detail/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/article/detail/:article_id',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
