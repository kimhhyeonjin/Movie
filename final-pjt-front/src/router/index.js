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
    name: 'main',
    component: MovieView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MypageView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/movie/detail/:movie_id',
    name: 'moviedetail',
    component: MovieDetail
  },
  {
    path: '/article/detail/:article_id',
    name: 'articledetail',
    component: ArticleDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
