<template>
  <div class="card" style="width: 18rem; background-color: black;">
    <!-- <h2>SearchList</h2> -->
    <div @click="goMovieDetail(result.id)">
      <div class="a">
        <img
          :src="`https://image.tmdb.org/t/p/original${result.poster_path}`"
          :alt="`${result.title}_poster`"
          width="180px"
          height="260px"
        >
      </div>
      <p class="card-title justify-content-center">{{ result.title }}</p>
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
.a img {
  transition: all 0.2s linear;
}
.a:hover img {
  transform: scale(1.4);
}
</style>