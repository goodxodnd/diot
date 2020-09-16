<template>
<div class="row" v-show="isLogin" >
    <div class="col-md-10"></div>
      <div class="col-md-2">
      <div style="position: relative;text-decoration:none; color:black; position:relative; left:7%;">
      <img src='../assets/header-user.png'>
              <b-dropdown size="lg"  variant="link" toggle-class="text-decoration-none" no-caret style="color:black;">
              <template v-slot:button-content>
              {{userDid}}
              </template>
              <b-dropdown-item><router-link to="/mypage">My Page</router-link></b-dropdown-item>
              <b-dropdown-item @click="logout()" >Sign out</b-dropdown-item>
              <div class="title-menu" >Sign out</div>
              </b-dropdown>

        <b-button class="alarm" @click="modalShow = !modalShow" style="background-color:transparent; border: solid transparent; position:relative; left:-8%;"><img src='../assets/noneAlarm.png'></b-button>
        <b-modal v-model="modalShow" hide-footer>
         <div class="d-block text-center">
          <h5>{{modalTitle}}</h5>
         </div>
         <div v-if="modalTitle ==='Owner Change Request!'">
         <b-button style="position: relative; color:white; background-color:#f04b4c; top:8px; left:34%; width:150px;"> <router-link to="/ownershipaccept" style="color:white;">OK</router-link></b-button>
         </div>


         <div  v-else-if="modalTitle ==='Owner Change Done'">
         <b-button @click="checkAccept()" style="position: relative; color:white; background-color:#f04b4c; top:8px; left:28%; width:45%;"> <router-link to="/ownershiprequest" style="color:white;">OK</router-link></b-button>
         </div>

         </b-modal>
      <img src='../assets/error.png' v-show="isAlarm" style="position:relative; left:80%; top:-38px;">
      </div>


      </div>
      </div>
</template>

<script>
import store from '../store'
import { mapState, mapActions } from "vuex"
import axios from 'axios'

  export default {
    data() {
      return {
        modalTitle: 'None Alarm',
        balance: 0,
        userDid: null,
        userEmail: null,
         modalShow: false,
         event: 500
      }
    },
    computed: {
        ...mapState(["isAlarm"]),
        ...mapState(["isLogin"])
    },
    methods: {
    ...mapActions(["logout"]),

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
      },
         checkEvent(){
            const did = sessionStorage.getItem("did")
            const token = sessionStorage.getItem("access_token")

          this.event = setInterval(() => {
            axios
              .get('http://localhost:9999/api/checkOwnerShip', { params: {},
                    headers:{
                    "Authorization" :token,
                    "did": did
                  },
                    })
              .then(response => {
                  console.log(response.data.event, response)

                  if (response.data.event == 'OwnerChangeRequest')
                  {
                      this.modalTitle = 'Owner Change Request!'
                      this.$store.commit("alarmOn")
                    }
                  })
              .catch(error => {
                console.log(error)
                })

            axios
              .get('http://localhost:9999/api/checkOwnerShipAccept', { params: {},
                    headers:{
                    "Authorization" :token,
                    "did": did
                  },
                    })
              .then(response => {
                  console.log(response.data.event, response)

                  if (response.data.event == 'OwnerAccept')
                  {
                      this.modalTitle = 'Owner Change Done'
                      this.$store.commit("alarmOn")
                    }
                  })
              .catch(error => {
                console.log(error)
                })

        }, 5000);
      },
      checkAccept() {

        const did = sessionStorage.getItem("did")
        const path = 'http://localhost:9999/api/checkAccept'
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

            this.modalTitle = 'None Alarm'
            this.$store.commit("alarmOff")

          })
          .catch(error => {
            console.log(error)
          })


      }
    },
    created() {



      this.getUserInfo()
      this.checkEvent()
    }
  }

</script>

<style>
</style>
