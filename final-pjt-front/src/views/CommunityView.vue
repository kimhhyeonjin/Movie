<template>
  <div>
    <h1>CommunityView</h1>
    <ArticleList
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
    <button @click="goToCreate">Create</button>
    
  </div>
</template>

<script>
import axios from 'axios'
import ArticleList from '@/components/ArticleList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityView',
  data() {
    return {
      articles: [],
    }
  },
  components: {
    ArticleList,
  },
  methods: {
    goToCreate() {
      this.$router.push({name: 'ArticleForm'})
    },
    getArticleList() {
      axios({
        method: 'get',
        url: `${API_URL}/communities/articles/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          this.articles = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getArticleList()
  }
}
</script>

<style>

</style>