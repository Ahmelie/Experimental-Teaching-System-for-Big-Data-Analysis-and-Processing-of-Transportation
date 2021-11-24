<template>
  <div id="map" class="map" style="height:700px" />
</template>

<script>

import 'ol/ol.css'
import TileLayer from 'ol/layer/Tile'
import { Heatmap as HeatmapLayer } from 'ol/layer'
import OSM from 'ol/source/OSM'
import VectorSource from 'ol/source/Vector'
import { Map, View, Feature } from 'ol'
import { Point } from 'ol/geom'
import { fromLonLat } from 'ol/proj'
import codeList from '@/assets/codeList.json'
import hatmapData from '@/assets/hatmapData.json'
export default {
  name: 'HotMap',
  components: {

  },
  data() {
    return {
      map: null,
      hotData: null
    }
  },
  mounted() {
    this.initMap() // 初始化地图
    this.addHeatMap() // 添加热力图数据
  },
  methods: {

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

          center: fromLonLat([113.994071, 22.575966]),
          zoom: 12,
          maxZoom: 19,
          minZoom: 5
        })
      })
      console.log('init finished')
    },
    addHeatMap() {
      const colors = ['#2200FF', '#16D9CC', '#4DEE12', '#E8D225', '#EF1616']

      console.log(hatmapData.data)
      this.layer = new HeatmapLayer({
        source: new VectorSource(),
        blur: 30,
        radius: 15,
        gradient: colors
      })
      this.map.addLayer(this.layer)
      this.AppendFeatures(hatmapData.data, colors, codeList, 50)
    },

    AppendFeatures(hatmapData, colors, points, max) {
      for (var i in hatmapData) {
        if (points[hatmapData[i].name]) {
          var coords = points[hatmapData[i].name]
          this.max = max
          var f = new Feature({
            geometry: new Point(
              fromLonLat([coords.center.lng, coords.center.lat])
            )
          })
          this.layer.getSource().addFeature(f)
        }
      }
    }

  }

}

</script>
<style scoped>
</style>
