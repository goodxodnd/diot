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
            <b-card class="authority-request-card01">
               <b-card-text>
               <div class="DeviceName"><b>{{DeviceName}}</b></div>
                <div>Owner: {{UserDid}}</div>
                {{Did}}
                <br>2020.06.15<br>
                 <b-button class= "ownership-btn" style="color:white; background-color:#f04b4c;">Ownership</b-button>
               </b-card-text>
            </b-card>
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-8">
          <b-card class="ownership-request-card05" title="Set Alram" sub-title="Device Info">
            <b-button class= "request-btn" @click="requestOwner({DeviceName,UserDid,Did})" style="color:white; background-color:#f04b4c;"> Request</b-button>
            <b-card-text> service-<br>2020.06.15</b-card-text>
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
        DeviceType: null,
        Did:null,
        UserDid:null
      }
    },
    methods: {
      ...mapActions(["requestOwner"]),
      getDeviceInfo() {
        const did = sessionStorage.getItem("did")
        const path = 'http://localhost:9999/api/getDeviceInfo'
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
            this.DeviceName = response.data[0].name
            this.DeviceType = response.data[0].deviceType
            this.Did = response.data[0].did
            this.UserDid = response.data[0].user_did

          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    created() {
      this.getDeviceInfo()
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
left: 35%;
background-color: #f04b4c;

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
.request-btn {
position: relative;
top: 40%;
left: 88%;
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
