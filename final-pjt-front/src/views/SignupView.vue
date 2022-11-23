<template>
  <div>
    <h1>Signup Page</h1>
    <br>
    <form @submit.prevent="signUp">
      <label for="username">&nbsp; &nbsp; &nbsp; &nbsp; 아이디 : &nbsp; </label>
      <input type="text" id="username" v-model="username"><br>
      <br>
      <label for="password1"> &nbsp; &nbsp; &nbsp; &nbsp;비밀번호 : &nbsp; </label>
      <input type="password" id="password1" v-model="password1"><br>
      <br>
      <label for="password2"> 비밀번호 확인 : &nbsp; </label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <br>
      <input type="submit" value="회원가입">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signUp', payload)
    }
  },
}
</script>

<style>

</style>