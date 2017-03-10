<template>
    <el-menu theme="light" class="nav" :default-active="activeIndex" mode="horizontal" v-show="Boolean($store.state.isLoggedIn)">
      <el-menu-item index="1"><router-link to="/dashboard"><i class="el-icon-arrow-right"></i>Overview</router-link></el-menu-item>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>Components</template>
        <el-menu-item index="2-1"><router-link to="/dashboard/details/companion">Companion Service</router-link></el-menu-item>
        <el-menu-item index="2-2"><router-link to="/dashboard/details/javaclient">Java Client</router-link></el-menu-item>
        <el-menu-item index="2-3"><router-link to="/dashboard/details/wakewordagent">WakeWordAgent</router-link></el-menu-item>
      </el-submenu>
      <el-menu-item index="3" style="float:right;" id="logout"><router-link to="/logout"><el-button type="primary">Logout</el-button></router-link></el-menu-item>
    </el-menu>
</template>

<style scoped>
.nav {
  border-radius: 0px;
  margin-top:0;
  padding:0px 10px 0 10px;
  margin:0 auto;
}

@media (max-width:400px) {
  .nav {
    padding:0;
  }
}

</style>

<script>
export default {
  data() {
    return {
      activeIndex: '1'
    }
  }
}
</script>
