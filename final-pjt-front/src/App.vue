<template>
  <div id="app">
    <!-- <nav>
      <router-link :to="{ name: 'MovieView' }">메인</router-link> |
      <router-link :to="{ name: 'SearchView' }">검색</router-link> |

      <span v-if="isLogin">
        <router-link :to="{ name: 'RecommendView' }">추천</router-link> |
        <router-link :to="{ name: 'CommunityView' }">게시판</router-link> |
        <router-link :to="{ name: 'LogoutView' }">로그아웃</router-link> |
        <router-link :to="{ name: 'MypageView', params: { username: `${user.username}`} }">{{ user.username }}</router-link>님 안녕하세요
      </span>

      <span v-else>
        <router-link :to="{ name: 'SignupView' }">회원가입</router-link> |
        <router-link :to="{ name: 'LoginView' }">로그인</router-link>
      </span>
      <br>
    </nav> -->
    <nav class="navbar navbar-expand-lg">
      <img src="@/assets/movie.png" @click="goToMain">
      &nbsp; &nbsp;
      <span v-if="isLogin">
        <!-- <router-link :to="{ name: 'MovieView' }"> 메인</router-link>  -->
        <router-link :to="{ name: 'SearchView' }">검색</router-link> 
        <router-link :to="{ name: 'RecommendView', params: { username: `${user.username}`} }">추천</router-link> 
        <router-link :to="{ name: 'CommunityView' }">게시판</router-link> 
        <router-link :to="{ name: 'LogoutView' }">로그아웃</router-link> 
        <router-link :to="{ name: 'MypageView', params: { username: `${user.username}`} }">{{ user.username }}</router-link><span id="text">님 안녕하세요</span>
      </span>

      <span v-else>
        <!-- <router-link :to="{ name: 'MovieView' }">메인</router-link>  -->
        <router-link :to="{ name: 'SearchView' }">검색</router-link> 
        <router-link :to="{ name: 'SignupView' }">회원가입</router-link> 
        <router-link :to="{ name: 'LoginView' }">로그인</router-link>
      </span>
      <br>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isLogin() {
      return this.$store.state.isLogin
    },
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    goToMain() {
      this.$router.push({name: 'MovieView'})
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
#app {
  font-family: 'Black Han Sans', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: black;
  padding: 20px;
}

#text {
  color: white;
}
nav {
  padding: 50px;
  background-color: black;
}

nav a {
  font-weight: bold;
  color: white;
  padding: 5px;
}

nav a.router-link-exact-active {
  color: gray;
}

</style>
