<template>
  <div id="app" class="row flex-xl-nowrap">
    <div id="Sidebar" class="col-12 col-md-3 col-xl-2"><Sidebar/></div>
    <div id="Content" class="col-12 col-md-9 col-xl-10 py-md-3 pl-md-5"><router-view/></div>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'

export default {
  components: {
    'Sidebar': Sidebar
  }
}
</script>

<style>

</style>
