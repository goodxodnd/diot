<template>
 <div class="Sidebar" v-show="isLogin">
  <div class="header">
       <svg class="lock" width="70%" height="70%" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M11.5 8h-7a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1zm-7-1a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h7a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-7zm0-3a3.5 3.5 0 1 1 7 0v3h-1V4a2.5 2.5 0 0 0-5 0v3h-1V4z"/>
       </svg>
       <div class="title">
         <router-link to="/dashboard" style="color:white;">
         diot
         </router-link>
       </div>
  </div>
  <div class="menu">
   <div class="title-menu">Device</div>
    <div class="main-menu">
      <router-link to="/devicesearch" style="color:white;">Search</router-link>
    </div>
    <div class="main-menu">
      <router-link to="/devicelist" style="color:white;">List</router-link>
    </div>
    <div class="main-menu">
      <router-link to="/deviceregister" style="color:white;">Register</router-link>
    </div>
    <br>
    <br>
   <div class="title-menu">Service</div>
    <div class="main-menu">
      <router-link to="/service" style="color:white;">My Service</router-link>
    </div>
    <div class="main-menu">
       <router-link to="/serviceregister" style="color:white;">Register</router-link>
    </div>
    <br>
    <br>
   <div class="title-menu">Authority</div>
    <div class="main-menu">
      <router-link to="/authorityrequest" style="color:white;">Request</router-link>
    </div>
    <div class="main-menu">
       <router-link to="/authorityaccept" style="color:white;">Accept</router-link>
    </div>
    <br>
    <br>
   <div class="title-menu">Ownership</div>
    <div class="main-menu">
      <router-link to="/ownershiprequest" style="color:white;">Request</router-link>
    </div>
    <div class="main-menu">
       <router-link to="/ownershipaccept" style="color:white;">Accept</router-link>
    </div>
    <br>
    <br>
   <div class="title-menu">Ticket</div>
    <div class="main-menu">
      <router-link to="/tierrequest" style="color:white;">My Ticket</router-link>
   </div>
    <div class="main-menu">
      <router-link to="/tieraccpet" style="color:white;">Register</router-link>
    </div>
    <br>
    <div class="title-menu" @click="logout()">Sign out</div>
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
.Sidebar {
background-color: pink;
position: relative;
    top: -0.5%;
    z-index: 1000;
    height:1127px;
}
.header {
background-color: #3d6098;
height: 80px;
}
.title {
font-size: 3.5em;
color: white;
position: relative;
top:-70%;
left: 40%;
}
.menu{
background-color:#213159;
height:1127px;
padding: 1.5rem;
}
.title-menu{
font-size: 1.5em;
font-weight: bold;
color: white;
position: relative;
left:10%;
top:0%;
}
.main-menu{
font-size: 1em;
color: white;
position: relative;
top:1%;
left:20%;
}
.lock {
color: white;
position: relative;
top: 10px;
left: -15%;
}

</style>
