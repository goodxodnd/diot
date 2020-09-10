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
import No from './components/No.vue'
import store from "./store";

Vue.use(Router)


const rejectAuthUser = (to, from, next) => {
    if (store.state.isLogin === true) {
        alert('Already Login')
        next("/dashboard")
    } else{
        next()
    }
}


const onlyAuthUser = (to, from, next) => {
    if (store.state.isLogin === false) {
        next("/signin")
    } else{
        next()
    }
}

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      beforeEnter: onlyAuthUser
    },
    {
        path:'/devicelist',
        name:'Devicelist',
        component: Devicelist,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/signin',
        name: 'Signin',
        component: Signin,
        beforeEnter: rejectAuthUser
    },
    {
        path:'/signup',
        name: 'Signup',
        component: Signup,
        beforeEnter: rejectAuthUser
    },
    {
        path:'/',
        name: 'Main',
        component: Main,
        beforeEnter: rejectAuthUser
    },
    {
        path:'/alarm',
        name: 'Alarm',
        component: Alarm,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/authorityaccept',
        name: 'Authorityaccept',
        component: Authorityaccept,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/authorityrequest',
        name: 'Authorityrequest',
        component: Authorityrequest,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/deviceregister',
        name: 'Deviceregister',
        component: Deviceregister,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/mypage',
        name: 'Mypage',
        component: Mypage,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/ownershipaccept',
        name: 'Ownershipaccept',
        component: Ownershipaccept,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/ownershiprequest',
        name: 'Ownershiprequest',
        component: Ownershiprequest,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/service',
        name: 'Service',
        component:Service,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/serviceregister',
        name: 'Serviceregister',
        component: Serviceregister,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/tieraccept',
        name: 'Tieraccept',
        component: Tieraccept,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/tiermanagement',
        name: 'Tiermanagement',
        component: Tiermanagement,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/tierrequest',
        name: 'Tierrequest',
        component: Tierrequest,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/tierserviceset',
        name: 'Tierserviceset',
        component: Tierserviceset,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/devicesearch',
        name: 'Devicesearch',
        component: Devicesearch,
        beforeEnter: onlyAuthUser
    },
    {
        path:'/no',
        name: 'No',
        component: No,
        beforeEnter: onlyAuthUser
    }

  ]
})
