<template>
    <div class="row">
        <div class="col-md-12">
          <div class="main-title">Device Registration</div>
        </div>
        <div class="col-md-2"></div>
        <div class="col-md-8">
           <div class="box">
            <div class="box-text">Registration</div>
            <div class="box-signup">
              <label class="txt01">Device Name</label>
                <input type="text" class="device" v-model="name" placeholder="Enter Device Name">
              <label class="txt02" >Device Type</label>
                <input class="type" type="text" v-model="deviceType" placeholder="Enter Device Type"/>
              <label class="txt03" >Device Information</label>
                <input class="info" type="text" v-model="info" placeholder="Enter Device Information"/>
              <label class="txt04">DID Number</label>
                <input class="did" type="text" v-model="did" placeholder="Enter DID Number"/>
              <label class="txt05">Public Key</label>
                <input class="key" type="text" v-model="publicKey" placeholder="Enter Public Key"/>
            </div>
            <b-button variant="light" @click="submit({name,deviceType,info,did,publicKey})" class="signup"style="color:white; background-color:#f04b4c;">R E G I S T R A T I O N</b-button></div>

          </div>
        <div class="col-md-2"></div>
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
        ...mapActions(["submit"]),




    }
}
</script>

<style>
.main-title {
position: relative;
top: 30px;
font-weight: bold;
font-size: 50px;
}
.box {
background-color: #E7E7E7;
position: relative;
top:70px;
left: 190px;
width:700px;
height:640px;
border-radius:50px;
}
.box-text {
font-size: 40px;
font-weight: bold;
position: relative;
top: 20px;
left: 130px;
}
.box-signin{
font-size: 20px;
}
.device {
width: 400px;
height: 45px;
position: relative;
top: 75px;
left: 18px;
}
.type {
width: 400px;
height: 45px;
position: relative;
top: 115px;
left: 130px;
}
.info {
width: 400px;
height: 45px;
position: relative;
top: 155px;
left: 130px;
}
.did {
width: 400px;
height: 45px;
position: relative;
top: 195px;
left: 130px;
}
.key {
width: 400px;
height: 45px;
position: relative;
top: 230px;
left: 130px;
}
.signup {
width: 400px;
height:50px;
position: relative;
top:270px;
left:130px;
font-size: 27px;
font-weight: bold;
background-color:#3d6098;
color: white;
}
.txt01 {
position: relative;
top: 30px;
left: 130px;
}
.txt02 {
position: relative;
top:115px;
left: -385px;
}
.txt03 {
position: relative;
top:158px;
left: -275px;
}
.txt04 {
position: relative;
top:198px;
left: -275px;
}
.txt05 {
position: relative;
top:235px;
left: -275px;
}


</style>
