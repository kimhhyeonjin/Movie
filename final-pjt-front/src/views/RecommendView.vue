<template>
  <div>
    <br>
    <!-- <h1>Recommend</h1> -->
    <br>
    <h1> 📽 {{ user.username }}님을 위한 추천 영화 </h1>
    <br>
    <h5> 👉 좋아요 누른 영화와 같은 장르를 추천!! 👈 </h5>
    <br>
    <!-- {{ movies }} -->
    <!-- {{ movies.title }} -->
    <div class="row row-cols-6 g-3 justify-content-center">
      <RecommendItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import RecommendItem from '@/components/RecommendItem'

export default {
  name: 'RecommendView',
  components: {
    RecommendItem,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    user() {
      return this.$store.state.user
    },
    movies() {
      return this.$store.state.recommendedMovies
    },
  },
  methods: {
    getRecommend() {
      if (this.isLogin === true) {
        this.getRecommendedMovies()
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    },
    getRecommendedMovies() {
      this.$store.dispatch('getRecommendedMovies', this.user.pk)
    },
  },
  created() {
    this.getRecommend()
  }
}
</script>

<style>

</style>