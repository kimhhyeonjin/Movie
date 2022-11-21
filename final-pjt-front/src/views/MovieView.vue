<template>
  <div>
    <h1>MovieView</h1>
    <UpcomingView/>
    <PopularView/>
    <TopratedView/>
  </div>
</template>

<script>
import UpcomingView from '@/components/UpcomingView'
import PopularView from '@/components/PopularView'
import TopratedView from '@/components/TopratedView'

export default {
  name: 'MovieView',
  components: {
    UpcomingView,
    PopularView,
    TopratedView
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      if (this.isLogin === true) { 
        this.$store.dispatch('getMovies')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    }
  }
}
</script>

<style>

</style>