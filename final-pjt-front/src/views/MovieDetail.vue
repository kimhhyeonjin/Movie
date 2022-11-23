<template>
  <div>
    <br>
    <h1>{{ movie?.title }}</h1>
    <br>
    <img
      :src="`https://image.tmdb.org/t/p/original${ movie?.poster_path }`"
      alt="movie_poster"
      width="360px"
      height="520px"
    >
    <br>
    <br>
    <div id="movieinfo">
      <p>개봉일: {{ movie?.release_date }}</p>
      <p>줄거리: {{ movie?.overview }}</p>
      <p>평점: {{ movie?.vote_average }}</p>
      <p>popularity: {{ movie?.popularity }}</p>
    </div>
    <br>
    <!-- <img
      :src="`https://image.tmdb.org/t/p/original${ movie?.backdrop_path }`"
      alt="movie_backdrop"
      width="180px"
      height="260px"
    > -->
    <form @submit.prevent="likeMovie">
      <input v-show="isLike" type="submit" value="좋아요 취소" style="background-color: yellow">
      <input v-show="!isLike" type="submit" value="좋아요" style="background-color: skyblue ">
    </form>
    <br>
    <ReviewList/>
    <ReviewForm/>
  </div>
</template>

<script>
import ReviewList from '@/views/ReviewList'
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
      isLike: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/`
      })
        .then((response) => {
          console.log(response)
          this.movie = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    likeMovie() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          console.log(response)
          this.isLike = response.data.isLike
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
#movieinfo {
  background-color: black;
  opacity: 0.5;
}
</style>