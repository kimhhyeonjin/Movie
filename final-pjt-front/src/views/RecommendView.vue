<template>
  <div>
    <br>
    <h1>Recommend</h1>
    <br>
    <h4> 👉 {{ user.username }}님을 위한 추천 영화 👈 </h4>
    <h5> 👉 좋아요 누른 영화와 같은 장르를 추천!! 👈 </h5>
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
    user() {
      return this.$store.state.user
    },
    movies() {
      return this.$store.state.recommendedMovies
    },
  },
  methods: {
    getRecommendedMovies() {
      this.$store.dispatch('getRecommendedMovies', this.user.pk)
    }
  },
  created() {
    this.getRecommendedMovies()
  }
}
</script>

<style>

</style>