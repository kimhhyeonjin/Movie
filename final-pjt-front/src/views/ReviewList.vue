<template>
  <div>
    <h3>리뷰 목록</h3>
    <div v-show="reviews">
      <ReviewListItem
        v-for="review in reviews"
        :key="review.id"
        :review="review"
        :movie_id="movie_id"
      />
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import ReviewListItem from '@/components/ReviewListItem'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem
  },
  data() {
    return {
      movie_id: this.$route.params.movie_id
    }
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    }
  },
  methods: {
    getReviewList() {
      this.$store.dispatch('getReviewList', `${this.$route.params.movie_id}`)
      // axios({
        //   method: 'get',
      //   url: `${API_URL}/movies/${this.$route.params.movie_id}/reviews/`
      // })
      //   .then((response) => {
        //     console.log(response)
      //     const reviews = response.data
      //     this.reviews = reviews
      //     this.$router.push({ name: 'MovieDetail', params: `{ movie_id: ${this.$route.params.movie_id} }` })
      //   })
      //   .catch((error) => {
        //     console.log(error)
      //   })
    }
  },
  created() {
    this.getReviewList()
  },
}
</script>

<style>

</style>