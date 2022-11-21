<template>
  <div>
    <h1>SearchView</h1>
    <SearchForm/>
    <div class="search">
      <h1>검색결과</h1>
      <div class="row mt-5" v-if="searchResult.length >= 1">
        <SearchList
          v-for="movie in searchResult"
          :movie="movie"
          :key="movie.id"
        />
      </div>
      <div id="result" class="row mt-5" v-else>
        <h1>검색 결과가 없습니다.</h1>
      </div>
    </div>
    <!-- <SearchForm/> -->
  </div>
</template>

<script>
import axios from 'axios'
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
      movies: [],
      keyword: this.$route.params.name,
    }
  },
  methods: {
    getMovie() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then((response) => {
          this.movies = response.data
        })
        .catch((error) => {
          console.log(error)
          alert('요청하신 결과가 없습니다.')
        })
    }
  },
  computed: {
    searchResult() {
      const result = []
      for (const movie of this.movies) {
        if (movie.overview.includes(this.keyword)) {
          result.push(movie)
        } else if (movie.title.includes(this.keyword)) {
          result.push(movie)
        }
      }
      return result
    }
  },
  mounted() {
    this.getMovie()
  }
}
</script>

<style>

</style>