<template>
<div class="container">
    <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-5">
          <div class="box03">
            <div class="box03-text">Manage your<br> professional diot</div>
            <div class="box03-subtext">sldkfnsldkf nlskdnfklsd sdlkfnsldkfs <br>sdkjfsdf skdjfnsdkj sdkjfnssz fsdsasd<br>
            sfsdfsdlkdnfsf sdlfknsdfk sdflksndfk<br> sdkjfskdjf sdfjs sdkjf. </div>
          </div>
        </div>
        <div class="col-md-5">
          <div class="box04">
            <div class="box04-text">Sign Up</div>
            <div class="box04-signup">
              <input class="id" v-model="did" name="did" type="text" placeholder="Enter DID Number"/>
              <input class="email" v-model="Email" name="Email" type="email" placeholder="Enter Email"/>
              <input class="password" v-model="password" name="password" type="password" placeholder="Enter Password"/>
              <input class="password02" v-model="passwordConfirm" name="passwordConfirm" type="password" placeholder="Renter Password"/>
            </div>
            <b-button @click="register({did,password,passwordConfirm,Email})" variant="light" class="signup">S I G N  U P</b-button></div>
          <div class="question">
            <a href="/signup.vue">Sign up here</a>
          </div>
        </div>
        <div class="col-md-1"></div>
    </div>
</div>
</template>

<script>
  import { mapState, mapActions } from "vuex"
  export default {
    data() {

    },
    computed: {
            ...mapState(["isLogin", "isLoginError"])
    },
    methods: {
        ...mapActions(["register"]),




    }
}
</script>

<style>
.box03 {
background-color: #3d6098;
position: relative;
top:145px;
width:475px;
height:500px;
border-top-left-radius:50px;
border-bottom-left-radius:50px;
}
.box03-text {
position: relative;
top: 130px;
left: 85px;
font-size: 30px;
font-weight: bold;
color: white;
}
.box03-subtext {
position: relative;
top: 150px;
left: 85px;
font-size: 15px;
color: white;
}
.box04 {
background-color: #E7E7E7;
position: relative;
top:145px;
width:475px;
height:500px;
border-top-right-radius:50px;
border-bottom-right-radius:50px;
}
.box04-text {
font-size: 40px;
font-weight: bold;
position: relative;
top: 40px;
left: 160px;
}
.box04-signin{
font-size: 20px;
}
.id {
width: 250px;
height: 45px;
position: relative;
top: 70px;
left: 110px;
}
.email {
width: 250px;
height: 45px;
position: relative;
top: 90px;
left: 110px;
}
.password {
width: 250px;
height: 45px;
position: relative;
top: 110px;
left: 110px;
}
.password02 {
width: 250px;
height: 45px;
position: relative;
top: 130px;
left: 110px;
}
.signup {
width: 250px;
height:50px;
position: relative;
top:170px;
left:110px;
font-size: 27px;
font-weight: bold;
background-color:#3d6098;
color: white;
}



</style>
