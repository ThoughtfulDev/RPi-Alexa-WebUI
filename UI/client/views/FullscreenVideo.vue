<template>
  <video playsinline autoplay muted loop id="bgvid">
    <source src="../../static/short.mp4" type="video/mp4">
  </video>
</template>

<style scoped>
video#bgvid {
    position: fixed;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: -100;
    -ms-transform: translateX(-50%) translateY(-50%);
    -moz-transform: translateX(-50%) translateY(-50%);
    -webkit-transform: translateX(-50%) translateY(-50%);
    transform: translateX(-50%) translateY(-50%);
    background-size: cover;
}

@media screen and (max-device-width: 800px) {
  #bgvid { display: none; }
}
</style>
