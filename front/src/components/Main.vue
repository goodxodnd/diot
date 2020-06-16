<template>
<div class="container">
    <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4" id="main">
          <div class="main-title">WELCOME TO DIOT</div>
            <router-link to="/signin">
              <b-button variant="light" class="sign-in">SIGN IN</b-button>
            </router-link>
            <router-link to ="signup">
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
.main-title {
font-size: 36px;
font-weight: bold;
color: black;
position: relative;
top:300px;
}
.sign-in {
font-weight: bold;
font-size: 25px;
width: 150px;
height: 50px;
position: relative;
top: 350px;

}
.sign-up {
font-weight: bold;
font-size: 25px;
background-color: #f04b4c;
color: white;
width: 150px;
height: 50px;
position: relative;
top: 350px;
left:20px;
}
</style>
