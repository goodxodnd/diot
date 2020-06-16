import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './components/Dashboard.vue'
import Devicelist from './components/Devicelist.vue'
import Signin from './components/Signin.vue'
import Signup from './components/Signup.vue'
import Alarm from './components/Alarm.vue'
import Authorityaccept from './components/Authorityaccept.vue'
import Authorityrequest from './components/Authorityrequest.vue'
import Deviceregister from './components/Deviceregister.vue'
import Devicesearch from './components/Devicesearch.vue'
import Main from './components/Main.vue'
import Mypage from './components/Mypage.vue'
import Ownershipaccept from './components/Ownershipaccept.vue'
import Ownershiprequest from './components/Ownershiprequest.vue'
import Service from './components/Service.vue'
import Serviceregister from './components/Serviceregister.vue'
import Tieraccept from './components/Tieraccept.vue'
import Tiermanagement from './components/Tiermanagement.vue'
import Tierrequest from './components/Tierrequest.vue'
import Tierserviceset from './components/Tierserviceset.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
        path:'/devicelist',
        name:'Devicelist',
        component: Devicelist
    },
    {
        path:'/signin',
        name: 'Signin',
        component: Signin
    },
    {
        path:'/signup',
        name: 'Signup',
        component: Signup
    },
    {
        path:'/main',
        name: 'Main',
        component: Main
    },
    {
        path:'/alarm',
        name: 'Alarm',
        component: Alarm
    },
    {
        path:'/authorityaccept',
        name: 'Authorityaccept',
        component: Authorityaccept
    },
    {
        path:'/authorityrequest',
        name: 'Authorityrequest',
        component: Authorityrequest
    },
    {
        path:'/deviceregister',
        name: 'Deviceregister',
        component: Deviceregister
    },
    {
        path:'/mypage',
        name: 'Mypage',
        component: Mypage
    },
    {
        path:'/ownershipaccept',
        name: 'Ownershipaccept',
        component: Ownershipaccept
    },
    {
        path:'/ownershiprequest',
        name: 'Ownershiprequest',
        component: Ownershiprequest
    },
    {
        path:'/service',
        name: 'Service',
        component:Service
    },
    {
        path:'/serviceregister',
        name: 'Serviceregister',
        component: Serviceregister
    },
    {
        path:'/tieraccept',
        name: 'Tieraccept',
        component: Tieraccept
    },
    {
        path:'/tiermanagement',
        name: 'Tiermanagement',
        component: Tiermanagement
    },
    {
        path:'/tierrequest',
        name: 'Tierrequest',
        component: Tierrequest
    },
    {
        path:'/tierserviceset',
        name: 'Tierserviceset',
        component: Tierserviceset
    },
    {
        path:'/devicesearch',
        name: 'Devicesearch',
        component: Devicesearch
    },

  ]
})
