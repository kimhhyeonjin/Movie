<template>
  <div>
    <!-- <h2>ArticleList</h2> -->
    <p @click="goArticleDetail(article.id)">
      {{ article.title }}
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
    }
  }
}
</script>

<style>

</style>