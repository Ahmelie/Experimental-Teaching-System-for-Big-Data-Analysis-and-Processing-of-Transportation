<template>
  <div class="app-container">
    <search-bar :type="1" />

    <div id="map" class="map" style="height:700px" />
  </div>
</template>

<script>
import { SearchBar } from '@/layout/components'
import 'ol/ol.css'
import TileLayer from 'ol/layer/Tile'
import OSM from 'ol/source/OSM'
import { Map, View } from 'ol'
import { fromLonLat } from 'ol/proj'

export default {
  name: 'Search',
  components: {
    SearchBar

  },
  data() {
    return {
      map: null
    }
  },
  mounted() {
    this.initMap() // 初始化地图
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
    }
  }
}
</script>
