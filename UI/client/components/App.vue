<template>
  <div id="app" class="page">
    <Navigation></Navigation>
    <router-view></router-view>
    <bottom></bottom>
  </div>
</template>

<style>
body {
  margin:0;
  padding:0;
  width:100%;
  background-color:#34495e;
  font-family: "Helvetica";
}
.page {
  text-align: center;
  margin:0 auto;
}

a {
  text-decoration: none;
}
</style>

<script>
import Navigation from '../views/Navigation'
import bottom from '../views/bottom'

export default {
  components: {
    Navigation,
    bottom
  }
}
</script>
