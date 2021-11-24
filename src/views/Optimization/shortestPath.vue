<template>
  <div>
    <search-bar :type="2" :start-point="startPoint" :end-point="endPoint" @changeChoose="changeChoose" @submit="submit" />
    <div id="container" class="map" style="height:700px" />
  </div>
</template>
<script type="text/javascript" src="//api.map.baidu.com/api?type=webgl&v=1.0&ak=gdksno2qBMGpegDlZ7Ycqos7hTTZ7ZIT"></script>
<script>

import { SearchBar } from '@/layout/components'
import 'ol/ol.css'
import TileLayer from 'ol/layer/Tile'
import OSM from 'ol/source/OSM'
import { Map, View, style, geom, control, layer, source, format } from 'ol'
import { toStringHDMS } from 'ol/coordinate'
import { toLonLat, Projection } from 'ol/proj'
import Overlay from 'ol/Overlay'

import { BMPGL } from "./bmpgl.js"
export default {
  name: 'ShortestPath',
  components: {
    SearchBar

  },
  data() {
    return {
      ak:'gdksno2qBMGpegDlZ7Ycqos7hTTZ7ZIT',
      map: null,
      startPoint: '',
      endPoint: '',
      choosePoint: 1
    }
  },
  mounted() {
    //this.initMap() // 初始化地图[116.301934,39.977552],[116.508328,39.919141]
        console.log('this.choosePoint:',this.choosePoint)
    this.init()
  },
  methods: {
    init(startPoint,endPoint) {
        var vm=this
        BMPGL(this.ak).then((BMapGL) => {
        // 创建地图实例
          this.map = new BMapGL.Map("container");
          this.map.centerAndZoom(new BMapGL.Point(114.08, 22.54), 12);
          this.map.enableScrollWheelZoom(true);

          var vm2=this
          this.map.addEventListener('click', function (e) {
            var temp = e.latlng.lng.toFixed(6) + ', ' + e.latlng.lat.toFixed(6)
            console.log("this.choosePoint:",vm.choosePoint)
            console.log(this.startPoint)
            if (vm.choosePoint === 1) { vm2.startPoint = temp } else if (vm.choosePoint === 2) { vm2.endPoint = temp }
          })
          //var p1 = new BMapGL.Point(116.301934,39.977552);
          //var p2 = new BMapGL.Point(116.508328,39.919141);

          var p1 = new BMapGL.Point(startPoint[0],startPoint[1]);
          var p2 = new BMapGL.Point(endPoint[0],endPoint[1]);
          var driving = new BMapGL.DrivingRoute(this.map, {renderOptions:{map: this.map, autoViewport: true}});
          driving.search(p1, p2);
      })
      .catch((err)=>{
        console.log(err)
      })
      console.log('init finished')

    },
    changeChoose(values) {
      this.choosePoint = values
    },
    submit(){
      //console.log(this.choosePoint)
      //console.log(this.startPoint)
      console.log(typeof(this.startPoint))
      var p1 = this.startPoint.split(",");
      var p2 = this.endPoint.split(",");
      this.init([parseFloat(p1[0]),parseFloat(p1[1])],[parseFloat(p2[0]),parseFloat(p2[1])]) // 初始化地图
    }

  }
}
</script>
