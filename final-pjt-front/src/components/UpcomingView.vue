<template>
  <div>
    <h3> 👉 Upcoming Movie 👈 </h3>
    <br>
    <br>
    <!-- {{ movies }} -->
    <div class="row row-cols-6 g-3 justify-content-center">
      <UpcomingListView
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
      />
    </div>
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