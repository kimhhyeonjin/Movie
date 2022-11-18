<template>
  <div>
    <h3>ReviewList</h3>
    <ReviewListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
    />
  </div>
</template>

<script>
import axios from 'axios'
import ReviewListItem from '@/components/ReviewListItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem
  },
  data() {
    return {
      reviews: []
    }
  },
  created() {
    this.getReviewList()
  },
  methods: {
    getReviewList() {
      console.log(this.reviews)
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/reviews/`
      })
        .then((response) => {
          console.log(response)
          const reviews = response.data
          this.reviews = reviews
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