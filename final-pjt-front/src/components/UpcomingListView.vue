<template>
  <div>
    <!-- <h3>UpcomingListView</h3> -->
    <div @click="goMovieDetail(movie.movie_id)">
    <img
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
      :alt="`${movie.title}_poster`"
      width="180px"
      height="260px"
    >
    </div>
    <br>
    {{ movie.title }}
    {{ movie.id }}
  </div>
</template>

<script>
export default {
  name: 'UpcomingListView',
  props: {
    movie: Object,
  },
  methods: {
    goMovieDetail(movie_id) {
      this.$router.push({ name: 'MovieDetail', params: {movie_id}})
    }
  }
}
</script>

<style>

</style>