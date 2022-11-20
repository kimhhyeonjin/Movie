<template>
  <div>
    <h1>Logout</h1>
  </div>
</template>

<script>
export default {
  name: 'LogoutView',
  created() {
    this.logout()
  },
  methods: {
    logout() {
      this.$store.dispatch('logOut')
    }
  }
}
</script>

<style>

</style>