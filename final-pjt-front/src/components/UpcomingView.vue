<template>
  <div>
    <h2>UpcomingView</h2>
    <UpcomingListView
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import UpcomingListView from '@/components/UpcomingListView'

export default {
  name: 'UpcomingView',
  components: {
    UpcomingListView,
  },
  computed: {
    movies() {
      return this.$store.state.upcomingMovies
    }
  },
  created() {
    this.$store.dispatch('getUpcomingMovies')
  }
}
</script>

<style>

</style>