<template>
  <div>
    <!-- <h1>Mypage</h1> -->
    <img src="@/assets/보노보노 프로필.png" style="width: 300px; height: 300px;">
    <br>
    <br>
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
        this.userData()
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView'})
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
          this.getMovie()
        })
        .catch(() => {
          this.$router.push('/404')
        })
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
        })
    },
  },
  created() {
    this.getUser()
  },
  beforeRouteUpdate(to, from, next){
    this.username = to.params.username
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