<template>
    <div class="row">
        <div class="col-md-12">
          <div class="ownership-main-title">My Device List</div>
        </div>
        <div class="col-md-11">
          <div class="device-table">

            <b-table-simple hover>
              <b-thead head-variant="secondary">
                <b-tr>
                <b-th>DeviceName</b-th>
                <b-th>DeviceType</b-th>
                <b-th>Info</b-th>
                <b-th>Device Did</b-th>
                <b-th>Owner Did</b-th>

                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr v-for="item in items">
                  <b-td>{{item.DeviceName}}</b-td>
                  <b-td>{{item.DeviceType}}</b-td>
                  <b-td>{{item.Info}}</b-td>
                  <b-td>{{item.Did}}</b-td>
                  <b-td>{{item.UserDid}}</b-td>



                </b-tr>
              </b-tbody>
            </b-table-simple>


          </div>
        </div>
        <div class="col-md-1"></div>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    data() {
      return {
        items: [],
      }
    },
    methods: {
      getMyDeviceList() {
        const did = sessionStorage.getItem("did")
        const path = 'http://localhost:9999/api/getMyDeviceList'
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

            for (var arr of response.data.payload) {

              var deviceInfo = {}

              deviceInfo['DeviceName'] = arr.name
              deviceInfo['DeviceType'] = arr.deviceType
              deviceInfo['Info'] = arr.info
              deviceInfo['Did'] = arr.did
              deviceInfo['UserDid'] = arr.user_did

              console.log('Info',deviceInfo)

              local_items.push(deviceInfo)
            }

            this.items = local_items
            console.log(this.items)

          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    created() {
      this.getMyDeviceList()
    }
  }
</script>

<style>
.device-list-title {
position: relative;
top: 30%;
  left: 2%;
font-weight: bold;
font-size: 3em;
}
.form-control {
  border: 1px solid #3d6098;
  box-shadow: 0 0 0 1px #3d6098;
  position: relative;
  top: 50%;
}
.service {
position: relative;
top: -15%;
left: 90.5%;
background-color: #f04b4c;
font-size: 20px;
width: 10%;
}
.using {
position: relative;
top: 50%;
left: 80%;
background-color: #f04b4c;
font-size: 20px;
width: 10%;
}
.device-list01 {
position: relative;
left:-0.6%;
top:40%;
  height:140px;
}
.device-list02 {
position: relative;
left:-0.6%;
top:60%;
  height:140px;
}
.device-list03 {
position: relative;
left:-0.6%;
top:80%;
  height:140px;
}
.device-list04 {
position: relative;
left:-0.6%;
top:100%;
  height:140px;
}
.content02{
  position:relative;
  top:-50px;
  left:110px;
}

</style>
