<template>
  <div>
    <h3>ArticleDetail</h3>
    <p>작성자 : 
      <span @click="goToProfile(user_info.username)">
        {{ user_info.username }}
      </span>
    </p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일자 : {{ article.created_at }}</p>
    <p>수정일자 : {{ article.updated_at }}</p>
    <!-- {{ user_info }} -->
    <div v-if="is_user">
      <button @click.prevent="updateArticle(article.id)">수정</button>
      <button @click.prevent="deleteArticle(article.id)">삭제</button>
    </div>
    <CommentList/>
    <CommentForm/>
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
      comments : null,
      content: null,
      is_user: false,
      user_info: null,
    }
  },
  components: {
    CommentForm,
    CommentList,
  },
  computed: {
    article() {
      return this.$store.state.article
    }
  },
  methods: {
    isUser() {
      if (this.article.user === this.$store.state.user.pk) {
        this.is_user = true
      }
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
          this.user_info = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    goToProfile() {
      this.$router.push({name: 'MypageView', params: {username: `${this.user_info.username}`}})
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
  },
  created() {
    this.getArticleDetail()
    this.getUserDetail()
    this.isUser()
  }
}
</script>

<style>

</style>