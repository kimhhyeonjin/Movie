<template>
  <div>
    <h2>SearchForm</h2>
    <form @submit.prevent="searchMovies">
      <label for="search"></label>
      <input type="text" v-model="content">
      <input type="submit" value="검색">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SearchForm',
  data() {
    return {
      content: null,
    }
  },
  methods: {
    searchMovies() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요!')
        return
      } else {
        this.$store.dispatch('searchMovies', content)
      }
    }
  }
}
</script>

<style>

</style>