<template>
  <div class="app-container">
    <el-table id="tab" :data="listTable" stripe style="width:100%">
      <el-table-column prop="ID" label="ID" align="center" />
      <el-table-column prop="vehicleNum" label="车牌号" align="center" />
      <el-table-column prop="Point" label="坐标" align="center" />
      <el-table-column prop="Time" label="时间" align="center" />
      <el-table-column prop="Direction" label="方向" align="center" />
      <el-table-column prop="Speed" label="速度" align="center" />
    </el-table>
  </div>
</template>

<script>
import outliersData from '@/assets/outliersData'
export default {
  name: 'Clearoutlier',
  data() {
    return {
      listTable: outliersData.data
    }
  },
  methods: {
  }
}
</script>
<style>
.app-container{
  padding:10px 15px;
}
#tab {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#tab td, #tab th {
  border: 1px solid #ddd;
  padding: 8px;
}

#tab tr:nth-child(even){background-color: #f2f2f2;}

#tab tr:hover {background-color: #ddd;}

#tab th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: center;
  background-color: #7ab49a;
  color: white;
}

</style>
