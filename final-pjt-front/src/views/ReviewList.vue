<template>
  <div class="review-list">
    <h3>리뷰 목록</h3>
    <div v-show="reviews">
      <ReviewListItem
        v-for="review in reviews"
        :key="review.id"
        :review="review"
        :movie_id="movie_id"
      />
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import ReviewListItem from '@/components/ReviewListItem'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem
  },
  data() {
    return {
      movie_id: this.$route.params.movie_id
    }
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    }
  },
  methods: {
    getReviewList() {
      this.$store.dispatch('getReviewList', `${this.$route.params.movie_id}`)
    }
  },
  created() {
    this.getReviewList()
  },
}
</script>

<style>
.review-list {
  position: absolute;
  top: 370px;
  left: 50%;
  width: 100%;
  transform: translate( -120px, 300px);
  text-align: start;
}
</style>