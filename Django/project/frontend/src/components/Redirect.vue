<template>
  <button type="button" @click="goTo">My cute cat</button>
</template>

<script>
  export default {
    name: "Redirect",
    props: {
      pathname: {
        type: String,
        required: true
      }
    },
    methods: {
      goTo() {
        this.$router.push({name: this.pathname});
      }
    }
  }
</script>

<style scoped lang="scss">
  button {
    width: 80%;
    background-color: transparent;
    color: green;
    border: 2px solid green;
    border-radius: 5px;
    min-height: 50px;
    text-transform: uppercase;
  }

  button:hover {
    background-color: green;
    color: white;
    border-color: white;
  }
</style>
