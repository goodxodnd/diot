<template>
    <div class="row">
        <div class="col-md-2">
          <div class= "ownership-sub-title">All Device List</div>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-9">
          <div class="ownership-main-title">Ownership Request</div>
        </div>
        <div class="col-md-2">
          <input class="form-control" type="text" placeholder="Search" aria-label="Search">
            <b-card class="authority-request-card01" title="Device name">
               <b-card-text>
               service-<br>2020.06.15<br>Tier<br>
                 <b-button class= "ownership-btn" style="color:white; background-color:#f04b4c;">Ownership</b-button>
               </b-card-text>
            </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8">
          <b-card class="ownership-request-card05" title="Set Alram" sub-title="Device Info">
            <b-button class= "request" @click="requestOwner()  style="color:white; background-color:#f04b4c;" >Request</b-button>
            <b-card-text> service-<br>2020.06.15<br>Tier</b-card-text>
          </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-2">
          <b-card class="ownership-request-card02" title="Device name">
            <b-card-text> service-<br>2020.06.15<br>Tier<br>
              <b-button class= "ownership-btn" style="color:white; background-color:#f04b4c;">Ownership</b-button>
            </b-card-text>

          </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8">
          <b-card class="ownership-request-card06" title="Service Info">
            <b-card-text></b-card-text>
          </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-2">
          <b-card class="ownership-request-card03" title="Device name">
            <b-card-text> service-<br>2020.06.15<br>Tier<br>
              <b-button class= "ownership-btn" style="color:white; background-color:#f04b4c;">Ownership</b-button>
            </b-card-text>
          </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8"></div>
        <div class="col-md-1"></div>
        <div class="col-md-2">
          <b-card class="ownership-request-card04" title="Device name">
            <b-card-text> service-<br>2020.06.15<br>Tier<br>
             <b-button class= "ownership-btn" style="color:white; background-color:#f04b4c;">Ownership</b-button>
            </b-card-text>
          </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8"></div>
        <div class="col-md-1"></div>
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
        ...mapActions(["requestOwner"]),




    }
}

</script>

<style>
.ownership-sub-title {
position: relative;
top: 70%;
font-weight: bold;
font-size: 1.6em;
}
.ownership-main-title {
position: relative;
top: 40%;
font-weight: bold;
font-size: 3em;
}
.form-control {
  border: 1px solid #3d6098;
  box-shadow: 0 0 0 1px #3d6098;
  position: relative;
  top: 50px;
  width: 250px;
}
.ownership-btn {
position: relative;
top: 40%;
left: 40%;
background-color: #f04b4c;
width:60%;
}
.ownership-request-card01 {
position: relative;
top:35%;
}
.ownership-request-card02 {
position: relative;
top:25%;
}
.ownership-request-card03 {
position: relative;
top:-60%;
}
.ownership-request-card04 {
position: relative;
top:-45%;
}
.request {
position: relative;
top: -60px;
left: 950px;
background-color: #f04b4c;
width:100px;
}
.reject {
position: relative;
top: 0px;
left: 850px;
background-color: #f04b4c;
width:100px;
}
.ownership-request-card05 {
position: relative;
top: 80px;
}
.ownership-request-card06 {
position: relative;
top: 120px;
height:450px;
}
</style>
