<template>
  <div class="app-container">
    <iframe src="analysis/outflowRange.html" scrolling="no" style="width: 100%;height: 656px;" frameborder="0" />
  </div>
</template>

<script>
import { SearchBar } from '@/layout/components'
import 'ol/ol.css'

export default {
  name: 'OutflowRange',
  components: {
    SearchBar
  },
  data() {
    return {
      map: null
    }
  },
  mounted() {
  },
  methods: {

  }
}
</script>
<style scoped>
iframe{
  /* padding: 10px; */
}
</style>
