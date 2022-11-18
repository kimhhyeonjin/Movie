<template>
  <div>
    <!-- <h3>TopratedListView</h3> -->
    <img
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
      :alt="`${movie.title}_poster`"
      width="180px"
      height="260px"
    >
    <br>
    {{ movie.title }}
  </div>
</template>

<script>
export default {
  name: 'TopratedListView',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>