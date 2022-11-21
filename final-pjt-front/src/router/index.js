import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import SearchView from '@/views/SearchView'
import RecommendView from '@/views/RecommendView'
import CommunityView from '@/views/CommunityView'
import MypageView from '@/views/MypageView'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import LogoutView from '@/views/LogoutView'
import MovieDetail from '@/views/MovieDetail'
import ArticleDetail from '@/views/ArticleDetail'
import ArticleForm from '@/views/ArticleForm'
import CommentList from '@/views/CommentList'
import ReviewList from '@/views/ReviewList'

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
    path: '/communities',
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
    path: '/logout',
    name: 'LogoutView',
    component: LogoutView
  },
  {
    path: '/movies/detail/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/movies/:movies_id/reviews/',
    name: 'ReviewList',
    component: ReviewList
  },
  {
    path: '/communities/articles/detail/:article_id',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/communities/articles/create_comment/',
    name: 'ArticleForm',
    component: ArticleForm
  },
  {
    path: '/communities/articles/:article_id/comments/',
    name: 'CommentList',
    component: CommentList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
