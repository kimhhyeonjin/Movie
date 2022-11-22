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
import ArticleList from '@/components/ArticleList'

export default {
  name: 'CommunityView',
  components: {
    ArticleList,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  methods: {
    goToCreate() {
      this.$router.push({name: 'ArticleForm'})
    },
    getArticleList() {
      this.$store.dispatch('getArticleList')
    }
  },
  created() {
    this.getArticleList()
  }
}
</script>

<style>

</style>