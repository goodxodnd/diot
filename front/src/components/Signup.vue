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
              <input class="id" v-model="did" name="did" type="text" placeholder="Enter Did "/>
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
top:45%;
left:-42%;
width:100%;
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
top:45%;
left:-50%;
width:100%;
height:500px;
border-top-right-radius:50px;
border-bottom-right-radius:50px;
}
.box04-text {
font-size: 40px;
font-weight: bold;
position: relative;
top: 5%;
left: 30%;
}
.box04-signin{
font-size: 20px;
}
.id {
width: 55%;
height: 45px;
position: relative;
top: 60px;
left: 22%;
}
.email {
width: 55%;
height: 45px;
position: relative;
top: 90px;
left: 22%;
}
.password {
width: 55%;
height: 45px;
position: relative;
top: 110px;
left: 22%;
}
.password02 {
width: 55%;
height: 45px;
position: relative;
top: 130px;
left: 22%;
}
.signup {
width: 60%;
height:50px;
position: relative;
left:23%;
font-size: 27px;
font-weight: bold;
background-color:#3d6098;
color: white;
}



</style>
