<template>
  <div class="search-bar">
    <van-radio-group v-if="type==1" v-model="radio">
      <div class="text-content" type="text" v-text="labelData" />
      <el-table id="tab" :data="tableData" max-height="660">
        <el-table-column prop="ID" label="ID" align="center" width="60" />
        <el-table-column v-if="tableData[0].Point" prop="Point" label="经纬度" align="center" />
        <el-table-column v-if="tableData[0].Shape_Area" prop="Shape_Area" label="面积" align="center" />
      </el-table>
    </van-radio-group>
    <van-form v-if="type==2" @submit="onSubmit">
      <van-radio-group v-model="choosePoint" class="choose-point" direction="horizontal">
        <van-radio class="radio-choose" name="1" @click="radioChage(1)">拾取起点</van-radio>
        <van-radio class="radio-choose" name="2" @click="radioChage(2)">拾取终点</van-radio>
      </van-radio-group>
      <van-field
        v-model="startPoint"
        label="起点："
        :rules="[{ required: true, message: '请选择或输入起点' }]"
      />
      <van-field
        v-model="endPoint"
        label="终点："
        :rules="[{ required: true, message: '请选择或输入终点' }]"
      />
      <div class="submit-button">
        <van-button block type="info" color="#42b983" native-type="submit">开始规划</van-button>
      </div>
    </van-form>
  </div>

</template>

<script>
import Vue from 'vue'
import 'vant/lib/index.css'
import { RadioGroup, Radio, Cell, CellGroup, Search, Toast, Form, Field, Button } from 'vant'
import { array } from 'jszip/lib/support'

Vue.use(Radio)
Vue.use(RadioGroup)
Vue.use(Cell)
Vue.use(CellGroup)
Vue.use(Search)
Vue.use(Toast)
Vue.use(Form)
Vue.use(Field)
Vue.use(Button)

export default {
  name: 'SearchBar',
  props: {
    labelData: {
      type: String,
      default: ''
    },
    tableData: {
      type: array,
      default: {}
    },
    type: {
      type: Number,
      default: 0
    },
    startPoint: {
      type: String,
      default: ''
    },
    endPoint: {
      type: String,
      default: ''
    },
    backPosition: {
      type: Number,
      default: 0
    },
    customStyle: {
      type: Object,
      default: function() {
        return {
          right: '50px',
          bottom: '50px',
          width: '40px',
          height: '40px',
          'border-radius': '4px',
          'line-height': '45px',
          background: '#e7eaf1'
        }
      }
    }

  },
  data() {
    return {
      value: '',
      radio: '0',
      choosePoint: '1'
    }
  },
  methods: {
    onSearch(val) {
      Toast(val)
    },
    onCancel() {
      Toast('取消')
    },
    onSubmit(values) {
      console.log(this.startPoint)
      console.log(this.endPoint)
      this.$emit('submit', this.startPoint, this.endPoint)
    },
    radioChage(values) {
      this.$emit('changeChoose', values)
    }
  }

}
</script>

<style lang="scss">

.search-bar {
  // transition: background .5s;
  width: 250px !important;
  background-color: rgba(179, 199, 185, 0.8);
  height: 100%;
  position: absolute;
  bottom: 0;
  right: 0;
  padding: 10px;
  color: #fff;
  z-index: 1000;
  .label{
    font-size: 16px;
    font-weight: 68 !important;
  }
}
.text-content{
  margin-bottom: 10px;
}
.choose-point{
  height: 44px;
}
.radio-choose{
  margin-left: 8px;
}
.van-form{
  background-color: #fff;
}
.van-field__label{
  width: auto !important;
  margin-right: 0 !important;
}

#tab td, #tab th {
  border: 1px solid #ddd;
  padding: 2px;
}

#tab tr:nth-child(even){background-color: #f2f2f2;}

#tab tr:hover {background-color: #ddd;}

#tab th {
  padding-top: 6px;
  padding-bottom: 6px;
  text-align: center;
  background-color: #7ab49a;
  color: white;
}
.el-table .cell{
  white-space:nowrap;
}
</style>
