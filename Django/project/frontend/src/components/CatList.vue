<template>
  <ul id="catList">
    <li v-for="cat in cats">
      <div v-if="cat.photo" class="photo-container">
        <img :src="cat.photo"
             alt="cat.name"
             height="200px"
             width="200px"/>
      </div>
      <div v-else class="photo-container">
        <img
          src="https://img.zcool.cn/community/01e8395970358ca8012193a3d4db11.jpg@3000w_1l_2o_100sh.jpg"
          alt="cat.name"
          height="200px"
          width="200px"/>
      </div>
      <div class="description">
        <div>
          <p><span class="grey"> Name </span>{{ cat.name }}</p>
          <p><span class="grey"> Owner </span>{{ cat.owner }}</p>
          <p><span class="grey"> Age </span>{{ cat.age }}</p>
        </div>
        <div class="more">
          <router-link :to="{ name: 'cutecat', params:{cat_id: cat.id} }">See more...</router-link>
        </div>

      </div>
    </li>
  </ul>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "CatList",
    computed: {
      ...mapGetters([
        'cats',
        'isLoading'
      ])
    }
  }
</script>

<style scoped lang="scss">
  #catList {
    min-width: 85%;
    padding-bottom: auto;
  }

  #catList li {
    list-style: none;
    display: flex;
    justify-content: space-between;
    border: solid 3px #e0e0e0;
    margin: 15px 0;
    box-shadow: 2px 3px #adadad;
  }


  li .description {
    flex: 2;
    padding: 10px 15px;
    background: #f5f5f5;
  }

  .description div p {
    text-transform: uppercase;
  }

  p span {
    font-size: 18px;
    color: darkgrey;
    padding: 0 10px 0 0;
  }

  .description .more {
    height: 35px;
    text-align: center;
    padding-top: 8px;
    font-size: 19px;
    background: #5bab74;
    border-radius: 5px;
  }

  .more:hover {
    background-color: #3e8353;
  }

  .more a {
    text-decoration: none;
    color: #f5f5f5;
  }

</style>
