<template>
  <div>
    <h2>PopularView</h2>
    <PopularListView
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import PopularListView from '@/components/PopularListView'

export default {
  name: 'PopularView',
  components: {
    PopularListView,
  },
  computed: {
    movies() {
      return this.$store.state.popularityMovies
    }
  },
  created() {
    this.$store.dispatch('getPopularMovies')
  }
}
</script>

<style>

</style>