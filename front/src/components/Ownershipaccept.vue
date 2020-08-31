<template>
    <div class="row">

        <div style="position: relative; top:2px; left: 94%;">
        <b-button class="alarm" @click="modalShow = !modalShow" style="background-color:transparent; border: solid transparent;"><img src='../assets/noneAlarm.png'></b-button>
        <b-modal v-model="modalShow" hide-footer>
         <div class="d-block text-center">
          <h5>{{modalTitle}}</h5>
         </div>
          <br><b-button style="position: relative; color:white; background-color:#f04b4c; left:27%;"> <router-link to="/ownershiprequest" style="color:white;">Request</router-link></b-button><b-button style="position: relative; color:white; background-color:#f04b4c; left:33%;"> <router-link to="/ownershipaccept" style="color:white;">Accept</router-link></b-button></b-modal>
        </div>
        <div style="position: relative; top:-6%; left:87%;">
              <b-dropdown size="lg"  variant="link" toggle-class="text-decoration-none" no-caret>
              <template v-slot:button-content>
              <img src='../assets/header-user.png'>
              </template>
              <b-dropdown-item><router-link to="/mypage">My Page</router-link></b-dropdown-item>
              <b-dropdown-item @click="logout()" >Sign out</b-dropdown-item>
              <div class="title-menu" >Sign out</div>
              </b-dropdown>
        </div>

        <div class="col-md-12">
          <div class="ownership-main-title">Ownership Accept</div>
        </div>
        <div class="col-md-11">
          <div class="accept-table">

            <b-table-simple hover>
              <b-thead head-variant="secondary">
                <b-tr>
                <b-th>DeviceName</b-th>
                <b-th>DeviceInfo</b-th>
                <b-th>Device Did</b-th>
                <b-th>Request User</b-th>
                <b-th></b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr v-for="item in items">
                  <b-td>{{this.DeviceName}}</b-td>
                  <b-td>{{this.DeviceInfo}}</b-td>
                  <b-td>{{this.DeviceDid}}</b-td>
                  <b-td>{{this.RequestUserName}}</b-td>
                  <b-td><b-button @click="acceptOwner({DeviceName,RequestUserName})" style="color:white; background-color:#f04b4c;">Accept</b-button></b-td>


                </b-tr>
              </b-tbody>
            </b-table-simple>


          </div>
        </div>
        <div class="col-md-1"></div>

</template>

<script>
import { mapState, mapActions } from "vuex"
import axios from 'axios'

export default {
    data() {
      return {
        isAlarm: false,
        DeviceName: null,
        UserName:null,
        RequestUserName:null,
        DeviceInfo: null,
        DeviceDid: null
      }
    },
    methods: {
      ...mapActions(["acceptOwner"]),
      ...mapActions(["logout"]),
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
            this.DeviceInfo = response.data.device_info
            this.DeviceDid = response.data.device_did

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
top: 300%;
left: -45%;
font-weight: bold;
font-size: 1.6em;
}
.ownership-main-title {
position: relative;
top: -10%;
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
top:80%;
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
