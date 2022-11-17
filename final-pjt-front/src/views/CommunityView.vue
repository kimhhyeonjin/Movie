<template>
  <div>
    <h1>CommunityView</h1>
    <ArticleForm/>
    <ArticleList/>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm'
import ArticleList from '@/components/ArticleList'

export default {
  name: 'CommunityView',
  components: {
    ArticleForm,
    ArticleList,
  }
}
</script>

<style>

</style>