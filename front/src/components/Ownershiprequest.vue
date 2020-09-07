<template>
    <div class="row">

        <div class="col-md-12">
          <div class="ownership-main-title">Ownership Request</div>
        </div>
        <div class="col-md-11">
          <div class="request-table">

            <b-table-simple hover>
              <b-thead head-variant="secondary">
                <b-tr>
                <b-th>DeviceName</b-th>
                <b-th>DeviceType</b-th>
                <b-th>Device Did</b-th>
                <b-th>Owner Did</b-th>
                <b-th></b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr v-for="item in items">
                  <b-td>{{item.DeviceName}}</b-td>
                  <b-td>{{item.DeviceType}}</b-td>
                  <b-td>{{item.Did}}</b-td>
                  <b-td>{{item.UserDid}}</b-td>
                  <b-td><b-button @click="requestOwner(item)" style="color:white; background-color:#f04b4c;">Request</b-button></b-td>


                </b-tr>
              </b-tbody>
            </b-table-simple>


          </div>
        </div>
        <div class="col-md-1"></div>
    </div>

</template>

<script>
import { mapState, mapActions } from "vuex"
import axios from 'axios'
import router from '../router'

export default {
    data() {
      return {
        isAlarm: false,
        items: [],
        DeviceName: null,
        DeviceType: null,
        Did:null,
        UserDid:null
      }
    },
    methods: {
      ...mapActions(["logout"]),
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
            var local_items = []
            for (var arr of response.data) {

              var deviceInfo = {}

              deviceInfo['DeviceName'] = arr.name
              deviceInfo['DeviceType'] = arr.deviceType
              deviceInfo['Did'] = arr.did
              deviceInfo['UserDid'] = arr.user_did

              local_items.push(deviceInfo)
            }

            this.items = local_items
            console.log(this.items)

          })
          .catch(error => {
            console.log(error)
          })
      },
      requestOwner(requestObj) {

          const token = sessionStorage.getItem("access_token")
          const did = sessionStorage.getItem("did")
          requestObj["didName"] = did;

          axios
            .post("http://localhost:9999/api/request_owner", requestObj)
            .then(res => {
              console.log(requestObj)
              let response = res.data

              if (response['code'] == '404'){
                console.log('error')
              }
              else {

                 this.$swal.fire({
                    icon: 'success',
                    title: 'Request Success!',
                    showConfirmButton: false,
                    timer: 3000
                      })

              }
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
font-size: 1.5em;
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
.request-table {
position: relative;
top:10%;
}
</style>
