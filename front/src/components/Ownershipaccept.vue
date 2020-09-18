<template>
    <div class="row">

        <div class="col-md-12">
          <div class="ownership-main-title">Ownership Accept</div>
        </div>
        <div class="col-md-11">
          <div class="accept-table">
            <b-table-simple hover>
              <b-thead head-variant="secondary">
                <b-tr>
                <b-th>Request User</b-th>
                <b-th>DeviceName</b-th>
                <b-th>DeviceInfo</b-th>
                <b-th>Device Did</b-th>
                <b-th></b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr >
                  <b-td>{{RequestUserName}}</b-td>
                  <b-td>{{DeviceName}}</b-td>
                  <b-td>{{DeviceInfo}}</b-td>
                  <b-td>{{DeviceDid}}</b-td>
                  <b-td> <b-button @click="researchDid(RequestUserName)" onClick="this.disabled=true;" style="color:white; background-color:#f04b4c;">View</b-button>
                         <b-button @click="acceptOwner({DeviceName,RequestUserName})" onClick="this.disabled=true;" style="color:white; background-color:#f04b4c;">Accept</b-button></b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>

        <div class="col-md-1"></div>
        <div >
        <b-modal v-model="modalShow" hide-footer>
         <div class="d-block text-center">
          <vue-json-pretty
                    :data="docu"
                    >
            </vue-json-pretty>

         </div>

        </b-modal>

        </div>

</template>

<script>
import { mapState, mapActions } from "vuex"
import axios from 'axios'
import router from '../router'
import store from '../store'
import VueJsonPretty from 'vue-json-pretty'


export default {
    data() {
      return {
        modalTitle: 'None info',
        isAlarm: false,
        DeviceName: null,
        UserName:null,
        RequestUserName:null,
        DeviceInfo: null,
        DeviceDid: null,
        modalShow: false,
        docu: null,
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
      },
      acceptOwner(acceptObj) {
          const token = sessionStorage.getItem("access_token")
          const did = sessionStorage.getItem("did")
          acceptObj["didName"] = did;
          axios
            .post("http://localhost:9999/api/change_owner", acceptObj)
            .then(res => {
              console.log(acceptObj)
              let response = res.data

              if (response['code'] == '404'){
                console.log('error')
              }
              else {
                this.$swal.fire({
                  icon: 'success',
                  title: 'Device Accept Success!',
                  showConfirmButton: false,
                  timer: 3000
                      })
                  router.push("/dashboard")
                  this.$store.commit("alarmOff")

              }
            })
        },
        researchDid(RequestUserName) {
          axios
          .get("http://localhost:8888/api/researchDid", {params: {},
          headers: {
            "did" : RequestUserName
          }
          })
          .then(res => {
              let response = res.data
              let result = res.data.payload



              if (response['code'] == '404'){
                console.log('error')
              }
              else {
                console.log(result)
                this.docu = result
                this.modalShow = !this.modalShow

              }
            })
          .catch(error => {
            console.log(error)
          })


        }


    },
    created() {
      this.find_event()
    },
    components: {
      VueJsonPretty
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
