<template>
  <div class="app-container">
    <div class="top">
      <input type="file" d="file_input" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" @change="importf(this)">
    </div>
    <el-table id="tab" :data="listTable" style="width:100%">
      <el-table-column prop="id" label="ID" align="center" />
      <el-table-column prop="vehicleNum" label="车牌号" align="center" />
      <el-table-column prop="startPoint" label="起点" align="center" />
      <el-table-column prop="endPoint" label="终点" align="center" />
      <el-table-column prop="startTime" label="开始时间" align="center" />
      <el-table-column prop="endTime" label="结束时间" align="center" />
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'ODTable',
  data() {
    return {
      listTable: []
    }
  },
  methods: {
    // 上传预览
    importf(obj) {
      const that = this
      this.file = event.currentTarget.files[0]
      var rABS = false // 是否将文件读取为二进制字符串
      var f = this.file
      var reader = new FileReader()
      // if (!FileReader.prototype.readAsBinaryString) {
      FileReader.prototype.readAsBinaryString = function(f) {
        var binary = ''
        var rABS = false // 是否将文件读取为二进制字符串
        var wb // 读取完成的数据
        var outdata
        var reader = new FileReader()
        reader.onload = function(e) {
          var bytes = new Uint8Array(reader.result)
          var length = bytes.byteLength
          for (var i = 0; i < length; i++) {
            binary += String.fromCharCode(bytes[i])
          }
          var XLSX = require('xlsx')
          if (rABS) {
            wb = XLSX.read(btoa(fixdata(binary)), {
              // 手动转化
              type: 'base64'
            })
          } else {
            wb = XLSX.read(binary, {
              type: 'binary'
            })
          }
          outdata = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
          const arr = []
          outdata.map(v => {
            const obj = {}
            obj.id = v.id
            obj.vehicleNum = v.vehicleNum
            obj.startPoint = v.startPoint
            obj.endPoint = v.endPoint
            obj.startTime = v.startTime
            obj.endTime = v.endTime
            arr.push(obj)
          })
          // 放入到element的table中显示出来
          that.listTable = arr
        }
        reader.readAsArrayBuffer(f)
        setTimeout(() => {
          alert('导入成功')
        }, 50)
      }
      if (rABS) {
        reader.readAsArrayBuffer(f)
      } else {
        reader.readAsBinaryString(f)
      }
    }
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

.top{
    margin-bottom: 10px;
}
</style>
