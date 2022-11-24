<template>
  <div>
    <h1>🙋커뮤니티</h1>
    <ArticleList
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
    <button @click="goToCreate" style="background-color: skyblue">등록</button>
    
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
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    getCommunity() {
      if (this.isLogin === true) { 
        this.getArticleList()
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    },
    goToCreate() {
      this.$router.push({name: 'ArticleForm'})
    },
    getArticleList() {
      this.$store.dispatch('getArticleList')
    },
  },
  created() {
    this.getCommunity()
  }
}
</script>

<style>

</style>