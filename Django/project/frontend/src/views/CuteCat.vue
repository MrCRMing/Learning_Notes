<template>
  <section class="container">
    <!--    <h1> Hi Guy </h1>-->
    <!--    <p>Welcome on an another page. Where lives the cuttest cat</p>-->
    <!--    <img-->
    <!--      src="data:image/jpeg;base64,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"-->
    <!--      alt="cute_cat"/>-->
    <idCard></idCard>
  </section>

</template>

<script>
  import idCard from '../components/IdCard'
  import {FETCH_A_CAT} from '../store/actions.type'
  import {mapGetters} from 'vuex'

  export default {
    name: "CuteCat",
    data() {
      return {}
    },
    components: {
      idCard
    },
    mounted() {
      this.$store.dispatch(FETCH_A_CAT, this.$route.params)
        .then(() => {
          console.log('YOU PI TOO');
        })
        .catch(() => {
          console.log('ERR : ', err);
        })
    }


  }
</script>

<style scoped lang="scss">
  .container {
    text-align: center;
    min-height: 77vh;
  }

  .container h1 {
    color: green;
  }

  .container p {
    margin: 0;
    color: lighten(green, 10%);
  }

  .container img {
    width: 100px;
    height: 100px;
  }

</style>
