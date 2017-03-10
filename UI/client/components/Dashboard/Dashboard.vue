<template>
  <div class="boxcontainer">
    <h1>Dashboard</h1>
    <h4>Quick Overview</h4>
    <hr />
    <CompanionService></CompanionService>
    <JavaClient></JavaClient>
    <WakeWordAgent></WakeWordAgent>
  </div>
</template>

<script>
import CompanionService from './CompanionService'
import JavaClient from './JavaClient'
import WakeWordAgent from './WakeWordAgent'

export default {
  components: {
    CompanionService,
    JavaClient,
    WakeWordAgent
  }
}
</script>

<style scoped>
.boxcontainer {
  max-width:400px;
  width:80%;
  background: #F9FAFC;
  padding:30px 15px 30px 15px;
  margin:50px auto;
  border-radius:5px;
  -webkit-box-shadow: 0px 0px 27px 2px rgba(0,0,0,0.40);
  -moz-box-shadow: 0px 0px 27px 2px rgba(0,0,0,0.40);
  box-shadow: 0px 0px 27px 2px rgba(0,0,0,0.40);
}

@media (max-width:600px) {
  .boxcontainer {
    width:85%;
  }
}

@media (max-width:380px) {
  .boxcontainer {
    width:100%;
    border-radius:0;
    -webkit-box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);
    -moz-box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);
    box-shadow: 0px 0px 0px 0px rgba(0,0,0,0);
  }
}
</style>
