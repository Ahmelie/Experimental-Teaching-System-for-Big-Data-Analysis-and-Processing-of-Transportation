<template>
  <div class="app-container">
    <div id="container" class="map" style="height:700px" />
  </div>
</template>

<script>

import 'ol/ol.css'
import TileLayer from 'ol/layer/Tile'
import OSM from 'ol/source/OSM'
import { Map, View } from 'ol'
import { fromLonLat } from 'ol/proj'
import { BMPGL } from './bmpgl.js'
export default {
  name: 'HotRoad',
  components: {

  },
  data() {
    return {
      map: null,
      ak: 'gdksno2qBMGpegDlZ7Ycqos7hTTZ7ZIT'
    }
  },
  mounted() {
    this.init() // 初始化地图
  },
  methods: {
    init(startPoint, endPoint) {
      BMPGL(this.ak).then((BMapGL) => {
        // 创建地图实例
        this.map = new BMapGL.Map('container')
        this.map.centerAndZoom(new BMapGL.Point(113.964704, 22.559514), 16)
        this.map.enableScrollWheelZoom(true)
        this.map.setTrafficOn() // 开启路况
      })
        .catch((err) => {
          console.log(err)
        })
      console.log('init finished')
    },
    initMap() {
      this.map = new Map({
        layers: [
          new TileLayer({
            source: new OSM()
          })
        ],
        target: 'map',
        view: new View({
          // projection: 'EPSG:4326',
          // center: [114.08, 22.54],
          // zoom: 12

          center: fromLonLat([114.08, 22.54]),
          zoom: 12,
          maxZoom: 19,
          minZoom: 5
        })
      })
      console.log('init finished')
    }

  }

}

</script>
<style scoped>
</style>
