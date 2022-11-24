<template>
  <div>
    <!-- test -->
    <div class="user-wrap">
      <div class="user-image">
        <img
          :src="`https://image.tmdb.org/t/p/original${ movie?.backdrop_path }`"
          alt="movie_backdrop"
          width="100%"
          height="100%"
        >
      </div>
      <div class="user-text">
        <p>🎬 {{ movie?.title }}</p>     
      </div>
    </div>
      <div class="user-poster-img">
        <img
        :src="`https://image.tmdb.org/t/p/original${ movie?.poster_path }`"
        alt="movie_poster"
        width="500px"
        height="750px"
        >
      </div>

    <div class="container">
      <h5>개봉일: {{ movie?.release_date }}</h5>
      <h5 id="overview">줄거리: {{ movie?.overview }}</h5>
      <h5>평점: {{ movie?.vote_average }}</h5>
      <h5>popularity: {{ movie?.popularity }}</h5>
    </div>
    <br>
    <!-- <img
      :src="`https://image.tmdb.org/t/p/original${ movie?.backdrop_path }`"
      alt="movie_backdrop"
      width="180px"
      height="260px"
    > -->
    <div class="like-form">
      <form @submit.prevent="likeMovie">
        <input v-show="isLike" type="submit" value="좋아요 취소" style="background-color: yellow">
        <input v-show="!isLike" type="submit" value="좋아요" style="background-color: skyblue ">
      </form>
    </div>
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
          this.checkIsLike()
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
    },
    checkIsLike() {

    }
  }
}
</script>

<style>
.container {
  position: absolute;
  top: 40%;
  left: 50%;
  width: 100%;
  transform: translate( -10%, 0%);
  font-size: 30px;
  text-align: start;
}

#overview {
  width: 1000px;
  word-break: break-word;
}

.square {
  border-radius: 5px;
  filter: blur(3px);
  opacity: 0.3;
}

.user-wrap {
  width: 100%;
  margin: 10px auto;
  position: relative;
}

.user-wrap img {
  width: 100%;
  vertical-align: start;
  opacity: 0.3;
}

.user-text {
  position: absolute;
  top: 40%;
  left: 50%;
  width: 100%;
  transform: translate( -45%, -250%);
  font-size: 80px;
  text-align: start;
}

.user-poster-img {
  position: absolute;
  top: 40%;
  left: 50%;
  width: 100%;
  transform: translate( -78%, -10%);
}

.like-form {
  position: absolute;
  top: 40%;
  left: 50%;
  width: 100%;
  transform: translate( -55%, 440%);
}
</style>