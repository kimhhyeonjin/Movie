<template>
  <div>
    <h1>RecommendView</h1>
    {{ user.username }}님이 좋아요 하신 영화를 기반으로 영화 추천
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