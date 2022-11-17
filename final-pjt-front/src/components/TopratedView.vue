<template>
  <div>
    <h2>TopratedView</h2>
    <TopratedListView
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
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
      return this.$store.state.movies
    }
  }
}
</script>

<style>

</style>