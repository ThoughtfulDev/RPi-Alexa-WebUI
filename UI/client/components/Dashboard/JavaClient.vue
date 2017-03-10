<template>
  <div>
    <el-form label-width="180px" class="javaform">
      <el-form-item label="Java Client">
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
      this.$store.state.axios.get('service/javaclient/status')
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
          self.$notify({
            title: 'Service started',
            message: 'Java Client has been successfully started',
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
.javaform {
  width:300px;
  margin:0 auto;
  text-align:center;
}
</style>
