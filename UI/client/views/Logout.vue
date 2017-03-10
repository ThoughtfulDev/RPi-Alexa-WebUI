<template>
</template>

<script>
import config from '../config'

export default {
  mounted: function() {
    this.$store.commit('LOGOUT')
    window.location.href = config['URL']
  }
}
</script>
