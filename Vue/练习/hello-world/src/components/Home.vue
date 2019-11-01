// 1模板：html结构
<template>
  <div id="home">
    {{title}}
    <app-header></app-header>
    <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/helloworld">Hello</router-link></li>
    </ul>
    <user v-bind:names="names" v-on:changeTitle="updateTitle($event)"></user>
    <app-footer></app-footer>
  </div>
</template>

//2行为：处理逻辑
<script>
import User from "./User.vue"
import Header from "./Header"
import Footer from "./Footer"

export default {
  name: 'home',
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
   
  },
    created(){
        this.$http.get("http://jsonplaceholder.typicode.com/users")
        .then((data)=>{
            this.names=data.body;
        })
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
