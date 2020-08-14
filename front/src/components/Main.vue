<template>
<div class="container">
    <div class="row">
        <div class="col-md-8" id="main">
          <div class="main-title01">WELCOME TO DIOT</div>
            <router-link to="/signin">
              <b-button variant="light" class="sign-in">SIGN IN</b-button>
            </router-link>
            <router-link to ="/signup">
              <b-button class="sign-up" style="color:white; background-color:#f04b4c;">SIGN UP</b-button>
            </router-link>
        </div>
        <div class="col-md-4"></div>
    </div>
</div>
</template>

<script>
</script>

<style>
.main-title01 {
font-size: 50px;
font-weight: bold;
color: black;
position: relative;
top:190%;
  left:10%;
}
.sign-in {
font-weight: bold;
font-size: 25px;
width: 200px;
height: 70px;
position: relative;
top: 250%;
  left:15%;

}
.sign-up {
font-weight: bold;
font-size: 25px;
background-color: #f04b4c;
color: white;
width: 200px;
height: 70px;
position: relative;
top: 250%;
left:20%;
}
.container{
-webkit-background-size: cover;
-moz-background-size: cover;
-o-background-size: cover;
background-size: cover;
position: relative;
z-index:10000;

/* Set rules to fill background */
min-height: 100%;
min-width:1024px;

/* Set up proportionate scaling */
width: 100%;
height: auto;

}
</style>
