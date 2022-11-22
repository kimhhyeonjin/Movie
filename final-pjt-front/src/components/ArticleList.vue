<template>
  <div>
    <!-- <h2>ArticleList</h2> -->
    <p @click="goArticleDetail(article.id)">
      <b>{{ article.title }}</b>
    </p>
    <p @click="goToProfile(username)">
      {{ article.user }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'ArticleList',
  props: {
    article: Object,
  },
  methods: {
    goArticleDetail(article_id) {
      this.$router.push({name: 'ArticleDetail', params: {article_id}})
    },
    goToProfile(username) {
      this.$router.push({name: 'MypageView', params: {username}})
    },
  },
}
</script>

<style>

</style>