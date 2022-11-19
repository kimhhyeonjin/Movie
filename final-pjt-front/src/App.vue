<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'MovieView' }">메인</router-link> |
      <router-link :to="{ name: 'SearchView' }">검색</router-link> |
      <router-link :to="{ name: 'RecommendView' }">추천</router-link> |
      <router-link :to="{ name: 'CommunityView' }">게시판</router-link> |
      <router-link :to="{ name: 'MypageView' }">마이페이지</router-link> |
      <router-link :to="{ name: 'SignupView' }">회원가입</router-link> |
      <router-link :to="{ name: 'LoginView' }">로그인</router-link> |
      {{ getUsername.username }}님 안녕하세요!
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  computed: {
    getUsername() {
      return this.$store.state.user
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
