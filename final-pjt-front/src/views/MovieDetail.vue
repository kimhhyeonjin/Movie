<template>
  <div>
    <h3>MovieDetail</h3>
    <p>제목: {{ movie?.title }}</p><br>
    <p>개봉일: {{ movie?.release_date }}</p><br>
    <p>줄거리: {{ movie?.overview }}</p><br>
    <p>평점: {{ movie?.vote_average }}</p><br>
    <p>popularity: {{ movie?.popularity }}</p><br>
    <img
      :src="`https://image.tmdb.org/t/p/original${ movie?.poster_path }`"
      alt="movie_poster"
      width="180px"
      height="260px"
    >
    <br>
    <img
      :src="`https://image.tmdb.org/t/p/original${ movie?.backdrop_path }`"
      alt="movie_backdrop"
      width="180px"
      height="260px"
    >
    <ReviewList/>
    <ReviewForm/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList'
import ReviewForm from '@/components/ReviewForm'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetail',
  components: {
    ReviewList,
    ReviewForm,
  },
  data() {
    return {
      movie: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}`
      })
        .then((response) => {
          console.log(response)
          this.movie = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style>

</style>