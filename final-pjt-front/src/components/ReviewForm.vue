<template>
  <div>
    <h3>리뷰 작성</h3>
    <form @submit.prevent="createReview">
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="1" v-model="content"></textarea><br>
      <input type="submit" id="submit" value="제출" style="background-color: skyblue ">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewForm',
  data() {
    return {
      content: null,
    }
  },
  methods: {
    createReview() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/create_review/`,
        data: {
          content: content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          this.$store.dispatch('getReviewList', `${this.$route.params.movie_id}`)
          this.content = null
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