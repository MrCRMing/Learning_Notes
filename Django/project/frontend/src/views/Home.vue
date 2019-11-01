<template>
  <section class="container">
    <!--    <h1> Welcome to your APP</h1>-->
    <!--    <redirectButton pathname="cutecat"></redirectButton>-->
    <h1> Our cutest cats </h1>
    <catList></catList>
  </section>
</template>

<script>

  // import redirectButton from '../components/Redirect'
  import {FETCH_CATS} from '../store/actions.type'
  import catList from '../components/CatList'
  import {mapGetters} from 'vuex'

  export default {
    name: "Home",
    components: {
      // redirectButton
      catList
    },
    mounted() {
      console.log("HAHAHHAHA");
      this.$store.dispatch(FETCH_CATS)
        .then(() => {
          console.log("YOU PI");
        })
        .catch((err) => {
          console.log("ERR : ", err);
        })
    }
  }
</script>

<style scoped lang="scss">

  .container {
    text-align: center;
  }

  .container h1 {
    color: green;
  }

</style>
