<template>
  <div>
    <h3>ArticleDetail</h3>
    <p>작성자 : {{ article.user }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일자 : {{ article.created_at }}</p>
    <p>수정일자 : {{ article.updated_at }}</p>
    <!-- <CommentList/> -->
    <h3>CommentList</h3>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
    <hr>
    <!-- <CommentForm/> -->
    <h3>CommentForm</h3>
    <form @submit.prevent="createComment">
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="5" v-model.trim="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
// import CommentForm from '@/components/CommentForm'
// import CommentList from '@/views/CommentList'
import CommentListItem from '@/components/CommentListItem'


const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: [],
      comments : null,
      content: null,
    }
  },
  components: {
    // CommentForm,
    // CommentList,
    CommentListItem,
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/communities/articles/${this.$route.params.article_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          this.article = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
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
    },
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
          this.getCommentList()
          this.content = null
        }) 
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getArticleDetail()
    this.getCommentList()
  }
}
</script>

<style>

</style>