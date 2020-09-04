<template>
  <div id="app" >
    <div class="row flex-xl-nowrap">
    <div id="Sidebar" class="col-12 col-md-3 col-xl-2">
    <Sidebar/>
    </div>
    <div id="Content" class="col-12 col-md-9 col-xl-10 py-md-3">
      <div class="col-12 col-md-9 col-xl-12 py-md-3 pl-md-5">
      <div id="Header" class="col-12 col-md-12">
      <Header/>
      </div>
        <router-view/>
      </div>
    </div>
   </div>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'
import Header from './components/Header.vue'


export default {
  components: {
    'Sidebar': Sidebar,
    'Header': Header,
  }
}
</script>

<style>

</style>
