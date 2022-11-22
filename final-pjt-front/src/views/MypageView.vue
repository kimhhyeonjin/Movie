<template>
  <div>
    <h1>Mypage</h1>
    <br>
    <!-- 자기자신을 팔로우하지 않도록 v-show 이용 -->
    <form v-show="followMe" @submit.prevent="followUser">
      <input v-show="isFollow" type="submit" value="팔로우 취소">
      <input v-show="!isFollow" type="submit" value="팔로우">
    </form>
    <br>
    <br>
    <h5>name : {{ username }}</h5>
    <br>{{ userdata }}
    <br>
    <br>
    <h5>내가 좋아요한 영화</h5>
    <h5>{{ userdata.like_movies }}</h5>
    <br>
    <h5>팔로잉 : {{ userdata.followings }}</h5>
    <br>
    <h5>팔로워 : {{ userdata.followers }}</h5>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MypageView',  
  data() {
    return {
      userdata: null,
      username: this.$route.params.username,
      isFollow: false,
      followMe: false,
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    isFollowMe() {
      if (this.username === this.user.username ) {
        this.followMe = false
      } else {
        this.followMe = true
      }
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
            })
            .catch((error) => {
              console.log(error)
            })
        })
        .catch((error) => {
          console.log(error)
        })
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
          console.log(response)
          this.userdata = response.data
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created() {
    this.isFollowMe()
    this.userData()
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