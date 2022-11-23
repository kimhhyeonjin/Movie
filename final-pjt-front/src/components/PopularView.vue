<template>
  <div>
    <h3> 👉 Popular Movie 👈 </h3>
    <br>
    <br>
    <div class="row row-cols-6 g-3 justify-content-center">
      <PopularListView
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import PopularListView from '@/components/PopularListView'

export default {
  name: 'PopularView',
  components: {
    PopularListView,
  },
  computed: {
    movies() {
      return this.$store.state.popularityMovies
    }
  },
  methods: {
    getPoppularMovies() {
      this.$store.dispatch('getPopularMovies')
    }
  },
  created() {
    this.getPoppularMovies()
  }
}
</script>

<style>

</style>