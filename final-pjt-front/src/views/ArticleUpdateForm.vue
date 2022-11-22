<template>
  <div>
    <h2>ArticleUpdateForm</h2>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model.trim="content"></textarea><br>
      <input id="submit" type="submit">
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
  methods: {
    loadArticle() {
      if (this.articleupdate === false) {
        this.articleupdate = true
      } else {
        const articleObj = {
          'title' : this.title,
          'content' : this.content
        }
        axios({
          method: 'get',
          url : `${API_URL}/communities/articles/${this.$route.params.article_id}`,
          data: {
            'articleObj' : articleObj
          }
        })
          .then((response) => {
            console.log(response)
          })
          .catch((error) => {
            console.log(error)
          })
        this.articleupdate = false
      }
    },
  },
  created() {
    this.loadArticle()
  },
}
</script>

<style>

</style>