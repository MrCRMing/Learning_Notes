<template>
  <div class="user">
      <h1>{{job}}</h1>
      <button v-on:click="changeTitle">改变值</button>
      <ul>
          <li v-for="(name,index) in names" :key="index">
              {{name.name}}
          </li>
      </ul>

  </div>
</template>
// 传值：string number boolean  --一个地方改变其他部分不变
// 传引用：array object  --一个地方改变全部改变
<script>
export default {
    name: 'user',
    data(){
        return{
            
            job:"student"
        }
    },
    // props:["names"]
    props:{
        names:{
            type:Array,
            required:true
        }
    },
    methods:{
        changeTitle:function(){
            this.$emit('changeTitle',"子组件向父组件传值");
        }
    }
    
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1{
    color: blue;
}

</style>
