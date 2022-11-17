<template>
  <div>
    <!-- <h3>TopratedListView</h3> -->
    {{ movie.title }}
  </div>
</template>

<script>
export default {
  name: 'TopratedListView',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>