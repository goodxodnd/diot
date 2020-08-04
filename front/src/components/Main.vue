<template>
<div class="container">
    <div class="row">
        <div class="col-md-8" id="main" img src="../assets/bg04.jpg">
          <div class="main-title01">WELCOME TO DIOT</div>
            <router-link to="/signin">
              <b-button variant="light" class="sign-in">SIGN IN</b-button>
            </router-link>
            <router-link to ="/signup">
              <b-button class="sign-up">SIGN UP</b-button>
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
top:350px;
  left:100px;
}
.sign-in {
font-weight: bold;
font-size: 25px;
width: 200px;
height: 70px;
position: relative;
top: 450px;
  left:120px;

}
.sign-up {
font-weight: bold;
font-size: 25px;
background-color: #f04b4c;
color: white;
width: 200px;
height: 70px;
position: relative;
top: 450px;
left:190px;
}
</style>
