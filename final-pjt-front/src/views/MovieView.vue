<template>
  <div>
    <div id="todaymovie" style="margin: 80px;">
      <h1>오늘의 영화</h1>
    </div>
    <UpcomingView/>
    <br>
    <PopularView/>
    <br>
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
#todaymovie {
  padding: 10px;
}
</style>