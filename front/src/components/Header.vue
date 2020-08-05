<template>
  <div class="row" v-show="isLogin">
      <div class="col-md-11" style="height:50px;"></div>
        <div class="col-md-1" style="height:50px;">
           <img src="../assets/alram.png" style="position:relative; left:20%;">
            <img src="../assets/header-user.png" style="position:relative; left:40%;">
        </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex"
  export default {

    data () {
      return{

      }
    },
    computed: {
        ...mapState(["isLogin"])
    },
    methods: {
        ...mapActions(["logout"]),



      }
    }
</script>

<style>
.main-header {
 height: 50px;
}
</style>
