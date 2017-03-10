<template>
  <div>
    <footer>
      <small>Proudly crafted by <a href="https://github.com/thoughtfuldev" target="new">ThoughtfulDev</a> |
        Made with <a href="https://vuejs.org/" target="new">Vue.js</a> & <a href="http://flask.pocoo.org/" target="new">Python Flask</a> |
        &copy; 2017 ThoughtfulDev</small>
    </footer>
  </div>

</template>

<style scoped>
footer {
  position:fixed;
  left:0px;
  bottom:0px;
  height:50px;
  width:100%;
  background:#2c3e50;
  padding-top:31px;
  color:white;
  text-align:left;
  padding-left:10px;
  padding-right:10px;
  -webkit-box-shadow: 0px 0px 10px rgba(0,0,0,.5);
  -moz-box-shadow: 0px 0px 10px rgba(0,0,0,.5);
  box-shadow: 0px 0px 10px rgba(0,0,0,.5);
}

/* IE 6 */
* html footer {
  position:absolute;
  top:expression((0-(footer.offsetHeight)+(document.documentElement.clientHeight ? document.documentElement.clientHeight : document.body.clientHeight)+(ignoreMe = document.documentElement.scrollTop ? document.documentElement.scrollTop : document.body.scrollTop))+'px');
}

footer a {
  color:#20A0FF;
}

footer a:hover {
  text-decoration:underline;
  color:#1D8CE0;
}
</style>
