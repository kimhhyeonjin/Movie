<template>
  <div>
    <!-- <h3>CommentListItem</h3> -->
    <p>{{ comment.content }}</p>
    <div v-if="is_user">
      <button @click.prevent="deleteComment">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  data() {
    return {
      is_user: false,
    }
  },
  props: {
    comment: Object,
    article_id: Number,
  },
  created() {
    this.isUser()
  },
  methods: {
    isUser() {
      if (this.comment.user === this.$store.state.user.pk) {
        this.is_user = true
      }
    },
    deleteComment() {
      axios({
        method: 'delete',
        url: `${API_URL}/communities/comments/${this.comment.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          console.log(response)
          this.$store.dispatch('getCommentList', `${this.article_id}`)
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