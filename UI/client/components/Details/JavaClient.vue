<template>
  <div class="boxcontainer">
    <h2 v-if="isOnline" id="online">Java Client is online</h2>
    <h2 v-if="!isOnline" id="offline">Java Client is offline</h2>
    <hr />
    <el-row :gutter="20">
      <!-- Log -->
      <el-col :span="16"><div class="grid-content bg-purple log" v-loading="isLoading" element-loading-text="Getting AWS Key...">
        <p v-html="strLog">

        </p>
      </div></el-col>
      <!-- Controls -->
      <el-col :span="8"><div class="grid-content controls">
        <el-tooltip class="item" effect="dark" content="Stops the Service" placement="bottom">
          <el-button type="danger" :disabled="Boolean(!isOnline || isLoading)" @click="stop()"><i class="material-icons">stop</i></el-button>
        </el-tooltip>
        <el-tooltip class="item" effect="dark" content="Starts the Service" placement="bottom">
          <el-button type="success" :disabled="Boolean(isOnline)"  @click="start()"><i class="material-icons">play_arrow</i></el-button>
        </el-tooltip>
        <el-tooltip class="item" effect="dark" content="Reloads the Log" placement="bottom">
          <el-button type="primary" :disabled="Boolean(!isOnline || isLoading)" @click="getLog()"><i class="material-icons">loop</i></el-button>
        </el-tooltip>
      </div></el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        isOnline: false,
        strLog: 'Loading...',
        isLoading: false
      }
    },
    mounted: function() {
      this.getStatus()
      if(this.isOnline === true) {
        this.getLog()
      }
      var self = this
      setInterval(function(){
        if(self.isOnline === true) {
          self.getLog()
        }
      }, 5000);
    },
    methods: {
      getStatus: function() {
        let self = this
        this.$store.state.axios.get('service/javaclient/status')
        .then(function (response) {
          self.isOnline = response.data['active']
          if(response.data['active'] == true) {
            setTimeout(function(){
              self.getLog()
            }, 1500)
          }
          else {
            self.strLog = 'Service is offline :('
          }
        })
        .catch(function (error) {
          this.$message.error(error);
          self.isOnline = false
        });
      },
      stop: function() {
        let self = this
        this.$store.state.axios.get('service/javaclient/stop')
        .then(function (response) {
          setTimeout(function(){
            self.$notify.info({
              title: 'Service stopped',
              message: 'Java Client has been stopped [PID: ' + response.data.pid + ']',
              type: 'success'
            });
            self.getStatus()
          }, 500);
        })
        .catch(function (error) {
          this.$message.error(error);
        });
      },
      start: function() {
        let self = this
        this.$store.state.axios.get('service/javaclient/start')
        .then(function (response) {
          setTimeout(function(){
            self.isLoading = true
            self.$notify({
              title: 'Service started',
              message: 'Java Client has been successfully started',
              type: 'success'
            });
            self.getStatus()
          }, 500);
          setTimeout(function(){
            self.isLoading = false
          }, 70000);
        })
        .catch(function (error) {
          this.$message.error(error);
        });
      },
      getLog: function() {
        let self = this;
        this.$store.state.axios.get('service/javaclient/log')
        .then(function (response) {
          self.strLog = response.data
        })
        .catch(function (error) {
          this.$message.error(error)
        })
      }
    }
  }
</script>

<style scoped>
.boxcontainer {
  max-width:800px;
  width:80%;
  background: #F9FAFC;
  padding:30px 15px 30px 15px;
  min-height:200px;
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

#offline {
  color:#e74c3c;
}

#online {
  color:#2ecc71;
}

 .bg-purple {
   background: #d3dce6;
   min-height:200px;
 }
 .grid-content {
   text-align:left;
   padding:5px 0px 0px 5px;
 }

 .controls {
   text-align: center;
 }
 .log {
   margin-top:7px;
   max-height:300px;
   overflow-y:auto;
   font-size:0.85em;
   padding:10px 5px 10px 20px;
   -moz-box-shadow:    inset 0 0 2px rgba(255,255,2,0.3);
   -webkit-box-shadow: inset 0 0 2px rgba(0,0,0,0.3);
   box-shadow:         inset 0 0 2px rgba(0,0,0,0.3);
 }
</style>
