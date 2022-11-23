<template>
  <div>
    <!-- <h2>ArticleList</h2> -->
    <br>
    <p @click="goArticleDetail(article.id)">
      <b>{{ article.title }}</b>
      <p>작성자 : {{ userDetail }}</p>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleList',
  props: {
    article: Object,
  },
  data() {
    return {
      userDetail: null,
    }
  },
  methods: {
    goArticleDetail(article_id) {
      this.$router.push({name: 'ArticleDetail', params: {article_id}})
    },
    getUserDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/userdetail/${this.article.user}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          this.userDetail = response.data.username
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getUserDetail()
  },
}
</script>

<style>

</style>