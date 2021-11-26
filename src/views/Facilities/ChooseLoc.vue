<template>
  <div>
    <search-bar :type="1" :table-data="tableData" :label-data="labelData" />
    <iframe src="Facilities/chooseLoc.html" scrolling="no" style="width: 100%;height: 655px;" frameborder="0" />
  </div>
</template>

<script>
import { SearchBar } from '@/layout/components'
import station from '@/assets/station'
export default {
  name: 'ChooseLoc',
  components: {
    SearchBar

  },
  data() {
    return {
      tableData: station.data,
      labelData: '经过位置优化算法计算得到的最终站点数量为33个。'
    }
  },
  mounted() {},
  methods: {

  }
}
</script>
<style scoped>
.app-container{
  padding: 10px 15px;
}
</style>
