<template>
  <div>
    <h3>MovieDetail</h3>
    <ReviewList/>
    <ReviewForm/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList'
import ReviewForm from '@/components/ReviewForm'

export default {
  name: 'MovieDetail',
  components: {
    ReviewList,
    ReviewForm,
  }
}
</script>

<style>

</style>