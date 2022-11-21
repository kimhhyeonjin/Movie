<template>
  <div>
    <h3>ArticleDetail</h3>
    <p>작성자 : {{ article.user }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일자 : {{ article.created_at }}</p>
    <p>수정일자 : {{ article.updated_at }}</p>
    <CommentList/>
    <CommentForm/>
  </div>
</template>

<script>
import axios from 'axios'
import CommentForm from '@/components/CommentForm'
import CommentList from '@/views/CommentList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: [],
    }
  },
  components: {
    CommentForm,
    CommentList,
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
    }
  },
  created() {
    this.getArticleDetail()
  }
}
</script>

<style>

</style>