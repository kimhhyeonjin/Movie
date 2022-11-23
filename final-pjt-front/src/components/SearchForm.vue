<template>
  <div>
    <!-- <h2>SearchForm</h2> -->
    <!-- <input type="text" v-model="keyword" placeholder="영화를 검색해보세요 :) "> -->
    <input type="text" v-model.trim="keyword" class="form-control" placeholder="영화 제목/내용을 검색해보세요 :)">
    <br>
    <button @click="GetKeyword" style="background-color: skyblue">검색!!</button>
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