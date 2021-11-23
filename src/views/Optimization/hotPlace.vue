<template>
  <div class="app-container">
    <!-- <search-bar /> -->

    <div id="map" class="map" style="height:700px" />
  </div>
</template>

<script>

import { SearchBar } from '@/layout/components'
import 'ol/ol.css'
import TileLayer from 'ol/layer/Tile'
import { Heatmap as HeatmapLayer } from 'ol/layer'
import OSM from 'ol/source/OSM'
import VectorSource from 'ol/source/Vector'
import { Map, View, Feature } from 'ol'
import { Point } from 'ol/geom'
import { fromLonLat } from 'ol/proj'

export default {
  name: 'HotPlace',
  components: {
    SearchBar

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
          projection: 'EPSG:4326',
          center: [114.08, 22.54],
          zoom: 12

          // center: fromLonLat([104.065735, 30.659462]),
          // zoom: 6.5,
          // maxZoom: 19,
          // minZoom: 5
        })
      })
      console.log('init finished')
    },
    addHeatMap() {
      const colors = ['#2200FF', '#16D9CC', '#4DEE12', '#E8D225', '#EF1616']
      const hatmapData = [
        { name: '成都市' },
        { name: '成都市' },
        { name: '成都市' },
        { name: '成都市' },
        { name: '绵阳市' },
        { name: '广安市' },
        { name: '雅安市' },
        { name: '自贡市' },
        { name: '自贡市' },
        { name: '自贡市' },
        { name: '自贡市' },
        { name: '自贡市' },
        { name: '自贡市' },
        { name: '自贡市' },
        { name: '宜宾市' },
        { name: '甘孜藏族自治州市' },
        { name: 'hot1' },
        { name: 'hot1' },
        { name: 'hot1' },
        { name: 'hot1' },
        { name: 'hot1' },
        { name: 'hot1' },
        { name: 'hot1' }
      ]
      const codeList = {
        成都市: { center: { lng: 104.061902, lat: 30.609503 }},
        广安市: { center: { lng: 106.619126, lat: 30.474142 }},
        绵阳市: { center: { lng: 104.673612, lat: 31.492565 }},
        雅安市: { center: { lng: 103.031653, lat: 30.018895 }},
        自贡市: { center: { lng: 104.797794, lat: 29.368322 }},
        宜宾市: { center: { lng: 104.610964, lat: 28.781347 }},
        hot1: { center: { lng: 113.930597, lat: 22.53003 }},
        甘孜藏族自治州市: {
          center: { lng: 101.592433, lat: 30.426712 }
        }
      }

      this.layer = new HeatmapLayer({
        source: new VectorSource(),
        blur: 30,
        radius: 15,
        gradient: colors
      })
      this.map.addLayer(this.layer)
      this.AppendFeatures(hatmapData, colors, codeList, 50)
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
