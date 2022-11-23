<template>
  <div>
    <h3> 👉 Top Rated Movie 👈 </h3>
    <br>
    <br>
    <div class="row row-cols-auto row-cols-md-3 g-3 justify-content-center" >
      <TopratedListView
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import TopratedListView from '@/components/TopratedListView'

export default {
  name: 'TopratedView',
  components: {
    TopratedListView
  },
  computed: {
    movies() {
      return this.$store.state.topRatedMovies
    }
  },
  methods: {
    getTopRatedMovies() {
      this.$store.dispatch('getTopRatedMovies')
    }
  },
  created() {
    this.getTopRatedMovies()
  }
}
</script>

<style>

</style>