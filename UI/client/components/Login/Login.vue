<template>
  <div>
    <div class="wrapper">
      <!--<FVideo></FVideo>-->
      <logo></logo>
      <el-form class="loginFrm">
        <el-form-item>
          <el-input placeholder="Enter your password" v-model="inpPass" type="password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="login()">Log me in!</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import config from '../../config'
import logo from '../../views/Header'
import FVideo from '../../views/FullscreenVideo'

export default {
  data() {
    return {
     inpPass: ''
   }
 },
 components: {
   logo,
   FVideo
 },
 methods: {
   login: function() {
     var bcrypt = require('bcryptjs');
     var salt = bcrypt.genSaltSync(10);
     if(bcrypt.compareSync(this.inpPass, config['SECRET'])) {
        var hash = bcrypt.hashSync(config['SECRET'] + config['HASHSECRET'], salt);
        this.$store.state.jsstore.set('user_session', { hash: hash })
        this.$store.dispatch('fetchSession')
        this.$router.push('/dashboard')
     }
     else {
       this.$message({
         message: 'Wrong password. Please try again',
         type: 'error',
         duration: 1500
       });
       this.inpPass = ''
       this.$store.state.jsstore.remove('user_session')
       this.$store.dispatch('fetchSession')
     }
   }
 },
 mounted: function() {
   if(this.$store.state.isLoggedIn) {
     this.$router.push('/dashboard')
   }
 }
}
</script>

<style scoped>
.loginFrm {
  max-width:500px;
  margin:0 auto;
}

.wrapper {
  width:90%;
  max-width:600px;
  background-color:#F9FAFC;
  margin:0 auto;
  padding:10px 10px 10px 10px;
  margin-top:9%;
  border-radius:5px;
  -webkit-box-shadow: 0px 0px 27px 2px rgba(0,0,0,0.40);
  -moz-box-shadow: 0px 0px 27px 2px rgba(0,0,0,0.40);
  box-shadow: 0px 0px 27px 2px rgba(0,0,0,0.40);
}
</style>
