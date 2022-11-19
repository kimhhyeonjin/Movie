<template>
  <div>
    <h3>CommentList</h3>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script>
import axios from 'axios'
import CommentListItem from '@/components/CommentListItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  data() {
    return {
      comments : null,
    }
  },
  methods: {
    getCommentList() {
      axios({
        method: 'get',
        url: `${API_URL}/communities/articles/${this.$route.params.article_id}/comments`,
        headers: {
        Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          this.comments = response.data
        }) 
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getCommentList()
  }
}
</script>

<style>

</style>