<template>
  <div>
    <!-- <h2>RecommendItem</h2> -->
    <br>
    <div @click="goMovieDetail(movie.id)">
    <img
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
      :alt="`${movie.title}_poster`"
      width="180px"
      height="260px"
    >
    </div>
    <p>{{ movie.title }}</p>
    <br>
  </div>
</template>

<script>
export default {
  name: 'RecommendItem',
  props: {
    movie: Object,
  },
  methods: {
    goMovieDetail(movie_id) {
      this.$router.push({ name: 'MovieDetail', params: {movie_id}})
    }
  },
}
</script>

<style>

</style>