<template>
  <div>
    <!-- <h4>ReviewListItem</h4> -->
    <p>{{ review.content }}</p>
    <div v-if="is_user">
      <button @click.prevent="updateReview">수정</button>
      <button @click.prevent="deleteReview">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  data() {
    return {
      is_user: false,
    }
  },
  props: {
    review: Object,
    movie_id: Number,
  },
  created() {
    this.isUser()
  },
  methods: {
    isUser() {
      if (this.review.user === this.$store.state.user.pk) {
        this.is_user = true
      }
    },
    updateReview() {
      axios({
        method: 'put',
        url: `${API_URL}/movies/reviews/${this.review.id}`,
        data: {
          content: this.review.content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/reviews/${this.review.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          console.log(response)
          this.$store.dispatch('getReviewList', `${this.movie_id}`)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  }
}
</script>

<style>

</style>