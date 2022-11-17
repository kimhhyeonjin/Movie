<template>
  <div>
    <h1>MovieView</h1>
    <UpcomingView/>
    <PopularView/>
    <TopratedView/>
  </div>
</template>

<script>
import UpcomingView from '@/components/UpcomingView'
import PopularView from '@/components/PopularView'
import TopratedView from '@/components/TopratedView'

export default {
  name: 'MovieView',
  components: {
    UpcomingView,
    PopularView,
    TopratedView
  },
}
</script>

<style>

</style>