<template>
  <div>
    <!-- <h2>SearchList</h2> -->
    <div @click="goMovieDetail(result.id)">
      <img
        :src="`https://image.tmdb.org/t/p/original${result.poster_path}`"
        :alt="`${result.title}_poster`"
        width="180px"
        height="260px"
      >
      <p>{{ result.title }}</p>
      <!-- <p>{{ result.id }}</p> -->

    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchList',
  props: {
    result: Object,
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