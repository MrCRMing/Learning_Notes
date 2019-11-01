// 1模板：html结构
<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

//2行为：处理逻辑
<script>
import User from "./components/User.vue"
import Header from "./components/Header"
import Footer from "./components/Footer"

export default {
  name: 'app',
  data(){
    return{
      title:"这是我的第一个vue脚手架项目",
      names:['Yoshi', 'Mario', 'Ryu'],
    }
  },
  components:{
    "user":User,
    "app-header":Header,
    "app-footer":Footer
  },
  methods:{
    updateTitle:function(title){
        this.title=title;
    }
  }

}
</script>
//3样式：解决样式
<style scoped>

h1{
  color:red;
}

body{
    margin: 0;
    font-family: 'Nunito SemiBold';
}
</style>
