<template>
  <div>
    <!-- <h3>LikeMovies</h3> -->
    <h5>{{ likeMovie.title }}</h5>
  </div>
</template>

<script>
export default {
  name: 'LikeMovies',
  props: {
    likeMovie: Object,
  }
}
</script>

<style>

</style>