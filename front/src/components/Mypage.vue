<template>
    <div class="row">
        <div class="col-md-12">
          <div class="page-title">My page</div>
        </div>
        <div class="col-md-2.5">
          <img src="../assets/big-user.png" style="position:relative; top:60%; left:10%; width:60%; ">
        </div>
        <div class="col-md-9.5">
          <div class="user-name">{{userDid}}</div><br>
          <div class="user-text"> Hello, Nice meet you !</div>
        </div>
        <div class="col-md-11">
            <b-card class="email-box" >
                <b-card-text class="email-info">
                  <img src="../assets/email.png" style="position:relative; width:3%;">
                  &nbsp;&nbsp;{{userEmail}}
                </b-card-text>
            </b-card>
        </div>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
      return {
        userDid: null,
        userEmail: null
      }
    },
    methods: {
      getUserInfo() {
        const did = sessionStorage.getItem("did")
        const path = 'http://localhost:9999/api/getUserInfo'
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
            this.userDid = response.data.did
            this.userEmail = response.data.email
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    created() {
      this.getUserInfo()
    }
  }
</script>

<style>
.page-title {
position: relative;
top: 30%;
font-weight: bold;
font-size: 3em;
}
.user-name {
position: relative;
top:90%;
left:-10%;
font-size:1.8em;
font-weight: bold;
}
.user-text {
position: relative;
top:85%;
left:-8%;
font-size:1.2em;
}
.email-box {
  position: relative;
  top:180%;
  height:80px;
}
.email-info {
  font-size: 1.2em;

}
</style>
