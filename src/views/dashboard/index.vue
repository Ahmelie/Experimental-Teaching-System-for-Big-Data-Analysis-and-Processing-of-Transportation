<template>
  <div class="dashboard-container">
    <!-- <component :is="currentRole" /> -->
    <h1 class="welcome-words">欢迎</h1>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  data() {
    return {
      currentRole: 'adminDashboard'
    }
  },
  computed: {
    ...mapGetters([
      'roles'
    ])
  },
  created() {
    if (!this.roles.includes('admin')) {
      this.currentRole = 'editorDashboard'
    }
  }
}
</script>
<style lang="scss">
.welcome-words{
  height: 100px;
  margin-top:100px;
  text-align: center;
}
</style>
