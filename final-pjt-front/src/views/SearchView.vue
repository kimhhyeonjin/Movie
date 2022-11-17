<template>
  <div>
    <h1>SearchView</h1>
    <SearchForm/>
    <SearchList/>
  </div>
</template>

<script>
import SearchForm from '@/components/SearchForm'
import SearchList from '@/components/SearchList'

export default {
  name: 'SearchView',
  components: {
    SearchForm,
    SearchList,
  }
}
</script>

<style>

</style>