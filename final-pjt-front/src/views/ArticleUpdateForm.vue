<template>
  <div>
    <h2>ArticleUpdateForm</h2>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model.trim="content"></textarea><br>
      <input id="submit" type="submit">
      <!-- {{ article }} -->
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleUpdateForm',
  data() {
    return {
      title : null,
      content: null,
      is_user: false,
      articleupdate : false,
    }
  },
  computed: {
    article() {
      return this.$store.state.article
    }
  },
  methods: {
    getArticleDetail() {
      this.$store.dispatch('getArticleDetail', `${this.$route.params.article_id}`)
      this.title = this.article.title
      this.content = this.article.content
    },
    updateArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/communities/articles/${this.$route.params.article_id}/`,
        data: {
          title: title,
          content: content,
          // user는 django에서 user_id를 뜻함
          user: this.$store.state.user.pk
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          this.$router.push({ name: 'ArticleDetail', params: `${this.$route.params.article_id}`})
        })
        .catch((error) => {
          console.log(error)
        })

    }
  },
  created() {
    this.getArticleDetail()
  },
}
</script>

<style>

</style>