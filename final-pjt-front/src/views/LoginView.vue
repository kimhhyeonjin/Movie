<template>
  <div>
    <h1>Login Page</h1>
    <br>
    <form @submit.prevent="logIn">
      <label for="username">username : &nbsp; </label>
      <input type="text" id="username" v-model="username"><br>
      <br>
      <label for="password"> password : &nbsp; </label>
      <input type="password" id="password" v-model="password"><br>
      <br>
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
    goToSignup() {
      this.$router.push({name: 'SignupView'})
    }
  }
}
</script>

<style>

</style>