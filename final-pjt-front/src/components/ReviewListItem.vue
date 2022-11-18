<template>
  <div>
    <!-- <h4>ReviewListItem</h4> -->
    <p>{{ review.content }}</p>
    <p></p>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  }
}
</script>

<style>

</style>