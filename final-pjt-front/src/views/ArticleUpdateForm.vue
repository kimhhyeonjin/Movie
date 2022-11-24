<template>
  <div id="update">
    <h2>게시글 수정</h2>
    <div>
      <form @submit.prevent="updateArticle">
        <div class="mb-3">
          <input type="text" v-model.trim="title" class="form-control" id="exampleFormControlInput1" placeholder="제목">
        </div>
        <div class="mb-3">
          <textarea class="form-control" id="exampleFormControlTextarea1" placeholder="내용" rows="3" v-model.trim="content"></textarea>
        </div>
        <input id="submit" type="submit" value="수정">
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleUpdateForm',
  data() {
    return {
      title : null,
      content: null,
      is_user: false,
      articleupdate : false,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    article() {
      return this.$store.state.article
    }
  },
  methods: {
    checkLogin() {
      if (this.isLogin === true) { 
        this.getArticleDetail()
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    },
    getArticleDetail() {
      this.$store.dispatch('getArticleDetail', `${this.$route.params.article_id}`)
      this.title = this.article.title
      this.content = this.article.content
    },
    updateArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/communities/articles/${this.$route.params.article_id}/`,
        data: {
          title: title,
          content: content,
          // user는 django에서 user_id를 뜻함
          user: this.$store.state.user.pk
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.push({ name: 'ArticleDetail', params: `${this.$route.params.article_id}`})
        })
        .catch((error) => {
          console.log(error)
        })

    }
  },
  created() {
    this.checkLogin()
  },
}
</script>

<style>
#update {
  width: 860px;
  display: inline-block;
}
</style>