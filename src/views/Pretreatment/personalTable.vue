<template>
  <!-- <div class="app-container"> -->
  <iframe src="pretreatment/personalTable.html" scrolling="no" style="width: 100%;height: 656px;" frameborder="0" />
  <!-- </div> -->
</template>

<script>
import { SearchBar } from '@/layout/components'
import 'ol/ol.css'

export default {
  name: 'RearsonalTable',
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
  padding: 10px 15px;
}
</style>
