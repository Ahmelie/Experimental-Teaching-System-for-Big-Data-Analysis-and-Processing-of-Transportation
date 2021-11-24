<template>
  <div class="app-container">

    <div class="top">
      <input type="file" d="file_input" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" @change="importf(this)">
    </div>

    <el-table id="tab" :data="listTable" stripe="true" style="width:100%">

      <el-table-column prop="id" label="id" align="center" />
      <el-table-column prop="vehicleNum" label="vehicleNum" align="center" />
      <el-table-column prop="startPoint" label="startPoint" align="center" />
      <el-table-column prop="endPoint" label="endPoint" align="center" />
      <el-table-column prop="startTime" label="startTime" align="center" />
      <el-table-column prop="endTime" label="endTime" align="center" />
    </el-table>
  </div>
</template>

<script>
import { SearchBar } from '@/layout/components'
import 'ol/ol.css'

// export default {
//   name: 'ODTable',
//   components: {
//     SearchBar
//   },
//   data() {
//     return {
//       map: null
//     }
//   },
//   mounted() {
//   },
//   methods: {

//   }
// }
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
      const inputDOM = this.$refs.inputer // 通过DOM取文件数据
      this.file = event.currentTarget.files[0]
      var rABS = false // 是否将文件读取为二进制字符串
      var f = this.file
      var reader = new FileReader()
      // if (!FileReader.prototype.readAsBinaryString) {
      FileReader.prototype.readAsBinaryString = function(f) {
        var binary = ''
        var rABS = false // 是否将文件读取为二进制字符串
        var pt = this
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
          // outdata就是你想要的东西 excel导入的数据
          outdata = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
          // excel 数据再处理
          const arr = []
          // 这里需要注意名字一定要和excel的内容的文字对上
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
    // 这里补个时间问题，excel的时间格式是序列号，如果用的上需要转化
    // 需要在这个位置加上调用方法
    // outdata.map(v => {
    //  let obj = {};
    //  obj.time= ExcelDateToJSDate(v.时间);
    //  arr.push(obj);
    // });
    // 这个方法暂时是目前找的比较好，日期不是很精确，精确不到秒（暂未查出小时和分钟出问题），excel日期序列号装换成时间格式，
    // function ExcelDateToJSDate(serial) {
    //  let utc_days = Math.floor(serial - 25569);
    //  let utc_value = utc_days * 86400;
    //  let date_info = new Date(utc_value * 1000);
    //  let fractional_day = serial - Math.floor(serial) + 0.0000001;
    //  let total_seconds = Math.floor(86400 * fractional_day);
    //  let seconds = total_seconds % 60;
    //  total_seconds -= seconds;
    //  let hours = Math.floor(total_seconds / (60 * 60));
    //  let minutes = Math.floor(total_seconds / 60) % 60;
    //  let ctime=new Date(date_info.getFullYear(), date_info.getMonth(), date_info.getDate(), hours, minutes, seconds);
    // 这是时间拼接，需要什么格式可以自行拼接
    //  return (ctime.getFullYear()+'-'+(ctime.getMonth()+1)+'-'+ctime.getDate());
    // }
    },
    // 上传按钮
    fileBtn() {
      // 上传这里可以分两种,一种是直接获取input的文件上传给后端，一种是我们已经解析了excel所以只要把listTable数组传给后端
      // 两种方法都可行，看自己需求
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
  text-align: left;
  background-color: #7ab49a;
  color: white;
}

.top{
    margin-bottom: 10px;
}
</style>
