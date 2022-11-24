<template>
  <div>
    <img src="@/assets/보노보노 프로필.png" style="width: 300px; height: 300px;">
    <br>
    <br>
    <!-- <h1>Mypage</h1> -->
    <h1> 😘 {{ username }} 의 프로필</h1>
    <!-- <br>{{ userdata }} -->
    <br>
    <h4> 👭🏼 팔로워 : {{ followingsCnt }}명</h4>
    <h4> 👬🏻 팔로잉 : {{ followersCnt }}명</h4>
    <br>
    <div v-show="likeMovies">
      <h3> 👉 좋아요 한 영화</h3>
      <!-- <h5>{{ userdata?.like_movies }}</h5> -->
      <LikeMovies
        v-for="likeMovie in likeMovies"
        :key="likeMovie.id"
        :likeMovie="likeMovie"
      />
    </div>
    <br>
    <!-- 자기자신을 팔로우하지 않도록 v-show 이용 -->
    <form v-show="followMe" @submit.prevent="followUser">
      <input v-show="isFollow" type="submit" value="팔로우 취소">
      <input v-show="!isFollow" type="submit" value="팔로우">
    </form>
  </div>
</template>

<script>
import LikeMovies from '@/components/LikeMovies'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MypageView',
  components: {
    LikeMovies
  },
  data() {
    return {
      username: this.$route.params.username,
      userdata: null,
      likeMovies: false,
      followers: false,
      followings: false,
      followersCnt: 0,
      followingsCnt: 0,
      isFollow: false,
      followMe: false,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    user() {
      return this.$store.state.user
    },
  },
  methods: {
    getUser() {
      if (this.isLogin === true) { 
        this.isFollowMe()
        this.userData()
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
      }
    },
    isFollowMe() {
      if (this.username === this.user.username ) {
        this.followMe = false
      } else {
        this.followMe = true
      }
    },
    userData() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/like/getuserid/${this.$route.params.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.userdata = response.data
          this.followers = response.data.followers
          this.followings = response.data.followings
          this.followersCnt = response.data.followers.length
          this.followingsCnt = response.data.followings.length
          this.checkIsFollow()
          this.getMovie()
        })
        .catch(() => {
          this.$router.push('/404')
          // console.log(error)
        })
    },
    checkIsFollow() {
      if (this.followings.includes(this.user.pk)) {
        this.isFollow = true
      } else {
        this.isFollow = false
      }
    },
    getMovie() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/like_movies/${this.userdata.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          if (response.data.length !== 0) {
            this.likeMovies = response.data
          }
        })
        .catch(() => {
          this.$router.push('/404')
          // console.log(error)
        })
    },
    followUser() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/like/getuserid/${this.$route.params.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          console.log(response)
          this.userdata = response.data
          const id = response.data.id
          axios({
            method: 'post',
            url: `${API_URL}/accounts/like/${id}/follow/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            },
          })
          .then((response) => {
            console.log(response)
            this.isFollow = response.data.isFollow
            this.userData()
          })
          .catch(() => {
            this.$router.push('/404')
            // console.log(error)
          })
        })
        .catch(() => {
          this.$router.push('/404')
          // console.log(error)
        })
    },
  },
  created() {
    this.getUser()
  },
  beforeRouteUpdate(to, from, next){
    this.username = to.params.username
    this.followMe = false
    next()
  },
}
</script>

<style>

html {
    height: 10%;
}

body {
    font-family: sans-serif;
    height: 10%;
    margin: 0;
}

.container {
    display: flex;
    height: 100%;
    flex-direction: column;
}

.image-upload {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.button {
    display: flex;
    justify-content: center;
}

label {
    cursor: pointer;
    font-size: 1em;
}

#chooseFile {
    visibility: hidden;
}

.fileContainer {
    display: flex;
    justify-content: center;
    align-items: center;
}

.fileInput {
    display: flex;
    align-items: center;
    border-bottom: solid 2px black;
    width: 60%;
    height: 30px;
}

#fileName {
    margin-left: 5px;
}

.buttonContainer {
    width: 10%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 10px;
    background-color: black;
    color: white;
    border-radius: 30px;
    padding: 10px;
    font-size: 0.8em;

    cursor: pointer;
}

.image-show {
    z-index: -1;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    width: 100%;
    height: 100%;
}

.img {
    position: absolute;
}

</style>