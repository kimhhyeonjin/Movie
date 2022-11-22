<template>
  <div>
    <!-- <h3>TopratedListView</h3> -->
    <div @click="goMovieDetail(movie.id)">
      <img
        :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
        :alt="`${movie.title}_poster`"
        width="180px"
        height="260px"
      >
      <p>{{ movie.title }}</p>
      <br>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopratedListView',
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