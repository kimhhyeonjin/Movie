<template>
  <div>
    <h1>RecommendView</h1>
    {{ user }}
    <RecommendItem/>
  </div>
</template>

<script>
import RecommendItem from '@/components/RecommendItem'

export default {
  name: 'RecommendView',
  components: {
    RecommendItem,
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  }
}
</script>

<style>

</style>