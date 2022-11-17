<template>
  <div>
    <!-- <h3>PopularListView</h3> -->
    {{ movie.title }}
  </div>
</template>

<script>
export default {
  name: 'PopularListView',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>