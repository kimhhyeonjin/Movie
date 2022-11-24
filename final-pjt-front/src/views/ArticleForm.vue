<template>
  <div>
    <h2>게시글 작성</h2>
    <div id="create">
      <form @submit.prevent="createArticle">
        <div class="mb-3">
          <!-- <label for="exampleFormControlInput1" class="form-label">제목</label> -->
          <input type="text" v-model.trim="title" class="form-control" id="exampleFormControlInput1" placeholder="제목">
        </div>
        <div class="mb-3">
          <!-- <label for="content">내용 : </label> -->
          <!-- <textarea id="content" cols="30" rows="10" v-model.trim="content"></textarea><br> -->
          <textarea class="form-control" id="exampleFormControlTextarea1" placeholder="내용" rows="3" v-model.trim="content"></textarea>
        </div>
        <input id="submit" type="submit" value="등록" style="background-color: skyblue">
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleForm',
  data() {
    return {
      title: null,
      content: null,    
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    checkLogin() {
      if (this.isLogin !== true) { 
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    },
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/communities/articles/`,
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
          this.$router.push({ name: 'CommunityView' })
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
#create {
  width: 860px;
  display: inline-block;
}
</style>