<template>
  <div class="app-header">
      <header>
      <h1>{{title}}</h1>
      </header>


  </div>
</template>

<script>
export default {
  name: 'app-header',
  data(){
      return {
          title:"Vue demo"
      }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
header{
    background: lightgreen;
    padding: 10px;
}
h1{
    color: #222;
    text-align: center;
}

</style>
