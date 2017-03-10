<template>
  <div>
    <el-form label-width="180px" class="wwaform">
      <el-form-item label="WakeWord Agent">
        <el-switch
          v-model="isOnline"
          on-color="#13ce66"
          off-color="#ff4949"
          @change="changeStatus"></el-switch>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
export default {
  data() {
    return {
      isOnline: false
    }
  },
  mounted: function() {
    this.getStatus()
  },
  methods: {
    changeStatus: function(newval) {
      if(newval) {
        this.start()
      }
      else {
        this.stop()
      }
    },
    getStatus: function() {
      let self = this
      this.$store.state.axios.get('service/wakewordagent/status')
      .then(function (response) {
        self.isOnline = response.data['active']
      })
      .catch(function (error) {
        this.$message.error(error);
        self.isOnline = false
      });
    },
    stop: function() {
      let self = this
      this.$store.state.axios.get('service/wakewordagent/stop')
      .then(function (response) {
        setTimeout(function(){
          self.$notify.info({
            title: 'Service stopped',
            message: 'WakeWord Agent has been stopped [PID: ' + response.data.pid + ']',
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
      this.$store.state.axios.get('service/wakewordagent/start')
      .then(function (response) {
        setTimeout(function(){
          self.$notify({
            title: 'Service started',
            message: 'WakeWord Agent has been successfully started',
            type: 'success'
          });
          self.getStatus()
        }, 500);
      })
      .catch(function (error) {
        this.$message.error(error);
      });
    }
  }
};
</script>

<style scoped>
.wwaform {
  width:300px;
  margin:0 auto;
  text-align:center;
}
</style>
