<template>
  <div>
    <!-- <h2>게시글 세부 정보</h2> -->
    <br>
    <span id="container">
    <h1>📋 {{ article.title }}</h1>
    <hr>
      <p>작성자 : 
        <span @click="goToProfile(article.username)">
          {{ article.username }}
        </span>
      </p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일자 : {{ article.created_at }}</p>
      <p>수정일자 : {{ article.updated_at }}</p>
      <div v-if="is_user">
        <button @click.prevent="updateArticle(article.id)" style="background-color: skyblue; border-radius: 7px">수정</button>
        <button @click.prevent="deleteArticle(article.id)" style="background-color: skyblue; border-radius: 7px">삭제</button>
      </div>
    </span>
    <hr>
    <CommentList/>
    <CommentForm/>
    <br>
    <div id="inputform">
      <form @submit.prevent="backToCommunity">
        <input type="submit" value="목록" style="background-color: skyblue; border-radius: 7px;">
      </form>
    </div>
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
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    checkLogin() {
      if (this.isLogin === true) { 
        this.getArticleDetail()
        this.$nextTick(function() {
          this.isUser()
        })
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    },
    isUser: function() {
      setTimeout(() => {
        if (this.article.username === this.$store.state.user.username) {
          this.is_user = true
        }
      }, 40)
    },
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
        .then(() => {
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
    this.checkLogin()
  },
}
</script>

<style>
#container {
  text-align: start;
  width: 500px;
  height: 250px;
}

#inputform {
  text-align: end;
}
</style>