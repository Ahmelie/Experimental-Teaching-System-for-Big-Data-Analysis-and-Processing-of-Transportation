<template>
  <div class="search-bar">
    <van-radio-group v-if="type==1" v-model="radio">
      <van-cell-group>
        <van-search
          v-model="value"
          show-action
          label="车牌号"
          placeholder=""
          @search="onSearch"
        >
          <template #action>
            <div @click="onSearch">查询</div>
          </template>
        </van-search>
        <van-cell title="周边搜索" clickable @click="radio = '1'">
          <select id="radius" οnchange="setSize(parseFloat(this.value))">
            <option name="radius" value="0.1">100</option>
            <option name="radius" value="0.2">200</option>
            <option name="radius" value="0.3">300</option>
          </select>
          <label>以内</label>
          <template #right-icon>
            <van-radio name="1" />
          </template>

        </van-cell>
        <van-cell title="多边形搜索" clickable @click="radio = '2'">
          <template #right-icon>
            <van-radio name="2" />
          </template>
        </van-cell>
        <van-cell title="起始点搜索" clickable @click="radio = '3'">
          <template #right-icon>
            <van-radio name="3" />
          </template>
        </van-cell>
        <van-cell title="终止点搜索" clickable @click="radio = '4'">
          <template #right-icon>
            <van-radio name="4" />
          </template>
        </van-cell>
        <van-cell title="属性查询" clickable @click="radio = '5'">
          <template #right-icon>
            <van-radio name="5" />
          </template>
        </van-cell>
      </van-cell-group>
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
</style>
