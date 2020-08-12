import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import axios from 'axios'

// test it.
Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        userInfo: null,
        isLogin: false,
        isLoginError: true
    },
    mutations: {
        //login success
        loginSuccess(state){
            state.isLogin = true,
            state.isLoginError = false
        },
        //login fail
        loginError(state){
            state.isLogin = false,
            state.isLoginError = true
        },
        logout(state) {
            state.isLogin = false,
            state.isLoginError = false,
            sessionStorage.removeItem("access_token");

        }
    },
    actions:{
        //try login
        login({ commit}, loginObj) {
          sessionStorage.setItem("did", loginObj["did"])
            // Login => token return
            axios
                .post("http://localhost:9999/api/signin", loginObj)
                .then(res => {
                  console.log("test")
                    let response = res.data
                    if(response['code'] == '200')
                        {
                        sessionStorage.setItem("access_token", response['access_token'])
                        let token = sessionStorage.getItem("access_token")
                        let config = {
                            headers: {
                                "Authorization": token
                                }
                            }
                            commit('loginSuccess')
                            router.push("/dashboard")
                        }
                    else {
                        alert(' Check your Id&PW 1 ');
                        }
                })
                .catch(() => {
                           alert(' Check your Id&PW 2');
                       })
            },
        register({ commit }, registerObj) {
          console.log(registerObj)
            if (registerObj['password'] == registerObj['passwordConfirm'])
            {
            axios
                .post("http://localhost:9999/api/register", registerObj)
                .then(res => {
                    let response = res.data
                    {
                        console.log(response)
                        if (response['code'] == '404') {
                            alert(' Already exist DID')
                        } else {
                            alert(' Register Success')
                            router.go(-1)
                        }
                    }
                })
            }
            else {
                alert('password is not same')
            }
        },
        submit({commit}, deviceObj) {
          const token = sessionStorage.getItem("access_token")
          const did = sessionStorage.getItem("did")
          deviceObj["didName"] = did;
          console.log(deviceObj)

          axios
            .post("http://localhost:9999/api/add_device", deviceObj)
            .then(res => {
              let response = res.data

              if (response['code'] == '404'){
                console.log('error')
              }
              else {
                console.log('device register success')
              }
            })
        },
        requestOwner({commit},requestObj) {
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
                console.log('device register success')
              }
            })

        }
        ,
        loginRefresh( {commit} ) {
            let token = sessionStorage.getItem("access_token");
            if (token != null) {
                commit("loginSuccess")
                router.push("/dashboard")
            }
            else
                commit('loginError')
            .catch(error => {
            console.log(error)
          })
        },
        logout({commit}) {
                commit("logout")
                router.push("/signin")
            },
    }
})
