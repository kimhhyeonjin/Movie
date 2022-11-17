<template>
  <div>
    <!-- <h3>UpcomingListView</h3> -->
    {{ movie.title }}
  </div>
</template>

<script>
export default {
  name: 'UpcomingListView',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>