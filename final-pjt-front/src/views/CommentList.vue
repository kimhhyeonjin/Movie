<template>
  <div id="commentlist">
    <!-- <h3>CommentList</h3> -->
    <h4>댓글 목록</h4>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      :article_id="article_id"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  data() {
    return {
      article_id: this.$route.params.article_id
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    comments() {
      return this.$store.state.comments
    }
  },
  methods: {
    checkLogin() {
      if (this.isLogin === true) { 
        this.getCommentList()
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    },
    getCommentList() {
      this.$store.dispatch('getCommentList', `${this.$route.params.article_id}`)
    }
  },
  created() {
    this.checkLogin()
  }
}
</script>

<style>
#commentlist {
  text-align: start;
}
</style>