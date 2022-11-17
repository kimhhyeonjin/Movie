<template>
  <div>
    <h3>ArticleDetail</h3>
    <CommentForm/>
    <CommentList/>
  </div>
</template>

<script>
import CommentForm from '@/components/CommentForm'
import CommentList from '@/components/CommentList'

export default {
  name: 'ArticleDetail',
  components: {
    CommentForm,
    CommentList,
  }
}
</script>

<style>

</style>