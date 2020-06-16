<template>
 <div class="Sidebar">
  <div class="header">
       <svg class="lock" width="60px" height="60px" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M11.5 8h-7a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1zm-7-1a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h7a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-7zm0-3a3.5 3.5 0 1 1 7 0v3h-1V4a2.5 2.5 0 0 0-5 0v3h-1V4z"/>
       </svg>
       <div class="title"> diot </div>
  </div>
  <div class="menu">
   <div class="title-menu">Device</div>
    <div class="main-menu">
      <router-link to="/devicesearch">Search</router-link>
    </div>
    <div class="main-menu">
      <router-link to="/devicelist">List</router-link>
    </div>
    <div class="main-menu">
      <router-link to="/deviceregister">Register</router-link>
    </div>
    <br>
    <br>
   <div class="title-menu">Service</div>
    <div class="main-menu">
      <router-link to="/service">My Service</router-link>
    </div>
    <div class="main-menu">
       <router-link to="/serviceregister">Register</router-link;>
    </div>
    <br>
    <br>
   <div class="title-menu">Authority</div>
    <div class="main-menu">
      <router-link to="/authorityrequest">Request</router-link>
    </div>
    <div class="main-menu">
       <router-link to="/authorityaccept">Accept</router-link>
    </div>
    <br>
    <br>
   <div class="title-menu">Ownership</div>
    <div class="main-menu">
      <router-link to="/ownershiprequest">Request</router-link>
    </div>
    <div class="main-menu">
       <router-link to="/ownershipaccept">Accept</router-link>
    </div>
    <br>
    <br>
   <div class="title-menu">Tier</div>
    <div class="main-menu">
      <router-link to="/tierrequest">Request</router-link>
   </div>
    <div class="main-menu">
      <router-link to="/tieraccpet">Accept</router-link>
    </div>
    <div class="main-menu">
      <router-link to="/tiermanagement">Management</router-link>
    </div>
    <div class="main-menu">
      <router-link to="/tierserviceset">Service Setting</router-link>
    </div>
</div>
 </div>
</template>


  </div>

 </div>
</template>

<script>
</script>

<style>
.Sidebar {
background-color: pink;
position: sticky;
    top: 4rem;
    z-index: 1000;
    height:1000px;
}
.header {
background-color: #3d6098;
height: 80px;
}
.title {
font-size: 60px;
color: white;
position: relative;
top:-65px;
left: 100px;
}
.menu{
background-color:#213159;
height:1000px;
padding: 1.5rem;
}
.title-menu{
font-size: 22px;
font-weight: bold;
color: white;
position: relative;
left:40px;
top:15px;
}
.main-menu{
font-size: 15px;
color: white;
position: relative;
top:20px;
left:55px;
}
.lock {
color: white;
position: relative;
top: 10px;
left: 30px;
}

</style>
