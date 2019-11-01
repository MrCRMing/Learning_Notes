import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import HelloWorld from './components/HelloWorld'
import Home from './components/Home'
import VueResource from'vue-resource'
Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(VueResource)
//定义全局组件
// import User from './components/User.vue'


//配置路由
const router=new VueRouter({
  routes:[
    {path:"/",component:Home},
    {path:"/helloworld",component:HelloWorld}
  ],
  mode:"history"
})
// Vue.component("user",User);
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

//index.html->main.js->App.vue