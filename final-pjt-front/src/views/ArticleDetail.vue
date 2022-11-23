<template>
  <div>
    <h3>ArticleDetail</h3>
    <p>작성자 : 
      <span @click="goToProfile(article.username)">
        {{ article.username }}
      </span>
    </p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일자 : {{ article.created_at }}</p>
    <p>수정일자 : {{ article.updated_at }}</p>
    <div v-if="is_user">
      <button @click.prevent="updateArticle(article.id)">수정</button>
      <button @click.prevent="deleteArticle(article.id)">삭제</button>
    </div>
    <br>
    <CommentList/>
    <CommentForm/>
    <br>
    <form @submit.prevent="backToCommunity">
      <input type="submit" value="목록">
    </form>
  </div>
</template>

<script>
import CommentForm from '@/components/CommentForm'
import CommentList from '@/views/CommentList'

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      is_user: false,
    }
  },
  components: {
    CommentForm,
    CommentList,
  },
  computed: {
    article() {
      return this.$store.state.article
    },
  },
  methods: {
    isUser: function() {
      setTimeout(() => {
        console.log(this.article.username)
        if (this.article.username === this.$store.state.user.username) {
          this.is_user = true
        }
        console.log(this.article.username)

      }, 40)
    },
    // isUser() {
    //   if (this.article.username === this.$store.state.user.username) {
    //     this.is_user = true
    //   }
    // },
    goToProfile() {
      this.$router.push({name: 'MypageView', params: {username: `${this.article.username}`}})
    },  
    getArticleDetail() {
      this.$store.dispatch('getArticleDetail', `${this.$route.params.article_id}`)
    },
    updateArticle() {
      this.$router.push({name: 'ArticleUpdateForm', params: `${this.$route.params.article_id}`})
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/communities/articles/${this.$route.params.article_id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          console.log(response)
          this.$router.push({name: 'CommunityView'})
        })
        .catch((error) => {
          console.log(error)
        })
    },
    backToCommunity() {
      this.$router.push({name: 'CommunityView'})
    }
  },
  created() {
    this.getArticleDetail()
    // this.$nextTick(function() {
    //   if (this.article.username === this.$store.state.user.username) {
    //     this.is_user = true
    //   }
    // })
  },
  mounted() {
    this.$nextTick(function() {
      this.isUser()
    })
  },
}
</script>

<style>

</style>