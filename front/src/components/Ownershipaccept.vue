<template>
    <div class="row">
        <div class="col-md-2">
          <div class= "ownership-sub-title">All Device List</div>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-9">
          <div class="ownership-main-title">Ownership Accept</div>
        </div>
        <div class="col-md-2">
            <b-card class="authority-request-card01">
               <b-card-text>
               <div class="DeviceName"><b>{{DeviceName}}</b></div>
               </b-card-text>
            </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8">
          <b-card class="ownership-request-card05">
            <b-card-text>
             <b>{{DeviceName}}</b>
             <br><b>{{RequestUserName}}</b>
            <b-button class= "accept-btn" @click="acceptOwner({DeviceName,RequestUserName})" style="color:white; background-color:#f04b4c; position:relative; left:81%;"> Accept</b-button>
            </b-card-text>
          </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-2">
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8">
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-2">
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8"></div>
        <div class="col-md-1"></div>
        <div class="col-md-2">
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8"></div>
        <div class="col-md-1"></div>
    </div>


</template>

<script>
import { mapState, mapActions } from "vuex"
import axios from 'axios'

export default {
    data() {
      return {
        DeviceName: null,
        UserName:null,
        RequestUserName:null
      }
    },
    methods: {
      ...mapActions(["acceptOwner"]),
      find_event() {
        const did = sessionStorage.getItem("did")
        const path = 'http://localhost:9999/api/find_event'
        const token = sessionStorage.getItem("access_token")

        axios
          .get(path, {params: {},
          headers: {
            "Authorization" :token,
            "did" : did
          }
          })
          .then(response => {
            console.log(response)
            this.DeviceName = response.data.device_name
            this.RequestUserName = response.data.RequestUserName
            this.UserName = response.data.UserName

          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    created() {
      this.find_event()
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
top: 50%;
left: 42%;
background-color: #f04b4c;

}
.ownership-request-card01 {
position: relative;
top:65%;
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
.accept-btn {
position: relative;
top: 40%;
left: 81%;
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
