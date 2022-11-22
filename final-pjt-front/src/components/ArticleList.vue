<template>
  <div>
    <!-- <h2>ArticleList</h2> -->
    <p @click="goArticleDetail(article.id)">
      <b>{{ article.title }}</b>
    </p>
    <p @click="goToProfile(userDetail)">
      {{ userDetail }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'ArticleList',
  props: {
    article: Object,
  },
  computed: {
    userDetail() {
      return this.$store.state.userDetail
    }
  },
  methods: {
    goArticleDetail(article_id) {
      this.$router.push({name: 'ArticleDetail', params: {article_id}})
    },
    goToProfile(username) {
      this.$router.push({name: 'MypageView', params: {username}})
    },
    getUserDetail() {
      this.$store.dispatch('getUserDetail', this.article.user )
    }
  },
  created() {
    this.getUserDetail()
  }
}
</script>

<style>

</style>