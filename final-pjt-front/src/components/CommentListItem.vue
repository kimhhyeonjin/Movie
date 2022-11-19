<template>
  <div>
    <!-- <h3>CommentListItem</h3> -->
    <p>{{ comment.content }}</p>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>