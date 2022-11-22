<template>
  <div>
    <h1>SearchView</h1>
    <SearchForm
      @get-keyword="searchMovie"
    />
    <!-- {{ searchResult }} -->
    <SearchList
      v-for="result in searchResult"
      :key="result.id"
      :result=result
    />
  </div>
</template>

<script>
// import axios from 'axios'
import SearchForm from '@/components/SearchForm'
import SearchList from '@/components/SearchList'

export default {
  name: 'SearchView',
  components: {
    SearchForm,
    SearchList,
  },
  data() {
    return {
      keyword: '',
    }
  },
  methods: {
    searchMovie(keyword) {
      this.keyword = keyword
    }
  },
  computed: {
    searchResult() {
      const result = []
      const movies = this.$store.state.movies
      for (const movie of movies)
        if (movie.title.includes(this.keyword)) {
          result.push(movie)
        } else if (movie.overview.includes(this.keyword)) {
          result.push(movie)
        }
      return result
    }
  }
}
</script>

<style>

</style>