<template>
  <div class="reviewform">
    <h3>리뷰 작성</h3>
    <form @submit.prevent="checkLogin">
      <textarea class="form-control" id="exampleFormControlTextarea1" placeholder="리뷰를 작성해주세요 :)" rows="1" v-model.trim="content" style="width: 1000px;"></textarea><br>
      <input type="submit" id="submit" value="등록" style="background-color: skyblue">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewForm',
  data() {
    return {
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
      if (this.isLogin === true) {
        this.createReview()
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    },
    createReview() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/create_review/`,
        data: {
          content: content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$store.dispatch('getReviewList', `${this.$route.params.movie_id}`)
          this.content = null
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }

}
</script>

<style>
.reviewform {
  position: absolute;
  top: 380px;
  left: 50%;
  width: 100%;
  transform: translate( -120px, 120px);
  text-align: start;
}
</style>