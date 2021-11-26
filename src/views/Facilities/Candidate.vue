<template>
  <div>
    <search-bar :type="1" :table-data="tableData" :label-data="labelData" />
    <iframe src="Facilities/candidate.html" scrolling="no" style="width: 100%;height: 655px;" frameborder="0" />
  </div>
</template>

<script>
import { SearchBar } from '@/layout/components'
import candidate from '@/assets/candidate'
export default {
  name: 'Candidate',
  components: {
    SearchBar

  },
  data() {
    return {
      tableData: candidate.data,
      labelData: '当前候选站点数量为932个。'
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
