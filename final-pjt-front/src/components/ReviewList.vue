<template>
  <h3>ReviewList</h3>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewList',
  data() {
    return {
      review: null,
    }
  },
  created() {
    this.getReviewList()
  },
  methods: {
    getReviewList() {
      console.log(this.$route.params.movie_id)
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/reviews/`
      })
        .then((response) => {
          console.log(response)
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