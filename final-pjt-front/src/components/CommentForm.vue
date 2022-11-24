<template>
  <div>
    <!-- <h3>CommentForm</h3> -->
    <form @submit.prevent="createComment">
      <br>
      <textarea class="form-control" id="exampleFormControlTextarea1" placeholder="댓글을 작성해주세요 :)" rows="1" v-model.trim="content"></textarea>
      <br>
      <input type="submit" id="submit" value="등록" style="background-color: skyblue">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: null,
    }
  },
  methods: {
    createComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요!')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/communities/articles/${this.$route.params.article_id}/create_comment/`,
        data: {
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          this.$store.dispatch('getCommentList', `${this.$route.params.article_id}`)
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