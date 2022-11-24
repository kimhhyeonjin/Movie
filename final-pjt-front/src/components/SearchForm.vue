<template>
  <div>
    <!-- <h2>SearchForm</h2> -->
    <!-- <input type="text" v-model="keyword" placeholder="영화를 검색해보세요 :) "> -->
    <div id="search"> 
      <input type="text" v-model.trim="keyword" class="form-control" placeholder="영화 제목/내용을 검색해보세요 :)">
    </div>
    <button @click="GetKeyword" style="background-color: skyblue; height: 45px; border-radius: 12px;">검색</button>
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
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    GetKeyword() {
      this.$emit('get-keyword', this.keyword)
      this.keyword = ''
    },
  },
  created() {
    this.getMovies()
  },
}
</script>

<style>
#search {
  width: 1550px;
  display: inline-block;
}
</style>