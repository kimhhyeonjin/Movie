<template>
  <div>
    <!-- <h2>RecommendItem</h2> -->
    <br>
    <div div class="card" style="width: 18rem; background-color: black;">
      <div @click="goMovieDetail(movie.id)">
        <div class="a">
          <img
            :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
            :alt="`${movie.title}_poster`"
            width="180px"
            height="260px"
          >
        </div>
      </div>
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
.a img {
  transition: all 0.2s linear;
}
.a:hover img {
  transform: scale(1.4);
}
</style>