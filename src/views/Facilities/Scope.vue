<template>
  <div>
    <search-bar :type="1" :table-data="tableData" :label-data="labelData" />
    <iframe src="Facilities/scope.html" scrolling="no" style="width: 100%;height: 655px;" frameborder="0" />
  </div>
</template>

<script>
import { SearchBar } from '@/layout/components'
import scope from '@/assets/scope'
export default {
  name: 'Scope',
  components: {
    SearchBar

  },
  data() {
    return {
      tableData: scope.data,
      labelData: '最终布设交通设施33个，每个多边形表示一个交通设施站点的服务范围。'
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
