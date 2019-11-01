<template>
  <div class="app-footer">
      <footer>
          <p>{{copyright}}</p>
      </footer>

  </div>
</template>

<script>
export default {
  name: 'app-footer',
  data(){
      return {
          copyright:'Copyright 2017 Vue Ninjas'
      }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
footer{
    background: #222;
    padding: 6px
}
p{
    color: lightgreen;
    text-align: center;
}

</style>
