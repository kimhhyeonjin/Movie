<template>
  <div>
    <h2>SearchForm</h2>
      <input 
        type="text"
        v-model="keyword"
      >
      <button @click="GetKeyword">Search</button>
  </div>
</template>

<script>
export default {
  name: 'SearchForm',
  data() {
    return {
      keyword: ''
    }
  },
  methods: {
    GetKeyword() {
      this.$emit('get-keyword', this.keyword)
      console.log(this.keyword)
      this.keyword = ''
    }
  }
}
</script>

<style>

</style>