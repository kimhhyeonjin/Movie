<template>
  <div>
    <br>
    <h1>Recommend</h1>
    <br>
    <h4> 👉 {{ user.username }}님을 위한 추천 영화 👈 </h4>
    <!-- {{ movies }} -->
    {{ movies.title }}
    <RecommendItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
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