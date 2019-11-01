<template>
  <div id="IdCard">
    <h1>{{ currentCat.name }}</h1>
    <div id="idPhoto">
      <div v-if="currentCat.photo" class="photocontainer">
        <img :src="currentCat.photo"
             alt="currentCat.name"
             height="250px"
             width="250px"/>
      </div>
      <div v-else class="photo-container">
        <img
          src="https://img.zcool.cn/community/01e8395970358ca8012193a3d4db11.jpg@3000w_1l_2o_100sh.jpg"
          alt="currentCat.name"
          height="250px"
          width="250px"/>
      </div>
    </div>
    <div class="description">
      <div>
        <p><span class="grey"> Owner </span>{{currentCat.owner }}</p>
        <p><span class="grey"> Age </span>{{ currentCat.age }} yo</p>
        <p><span class="grey"> Color </span>{{ getColor }}</p>
        <p><span class="grey"> Mood </span>{{ getMood }} </p>
        <p><span class="grey"> Favorite toy </span>{{ currentCat.toy }}</p>
      </div>
    </div>
  </div>

</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "IdCard",
    computed: {
      ...mapGetters([
        'currentCat',
        'isLoading'
      ]),
      getColor() {
        let color = '';
        if (this.currentCat.colors === "BLK") {
          color = 'Black';
        } else if (this.currentCat.colors === "GRY") {
          color = 'Grey';
        } else if (this.currentCat.colors === "RED") {
          color = 'Red';
        } else if (this.currentCat.colors === "WHE") {
          color = 'White';
        }else if (this.currentCat.colors === "BRW") {
          color = 'Brown';
        }

        return color;
      },
      getMood() {
        let mood = '';
        if (this.currentCat.mood === "HAY") {
          mood = 'Happy';
        } else if (this.currentCat.mood === "GRY") {
          mood = 'Grumpy';
        } else if (this.currentCat.mood === "BAD") {
          mood = 'Bad';
        }
        return mood;
      }
    }
  }
</script>

<style scoped lang="scss">
  h1 {
    color: green;
    text-transform: uppercase;
    text-align: center;
    font-size: 40px;
  }

  h1 #idPhoto {
    text-align: center;
  }

  h1 .description {
    flex: 2;
    padding: 20px 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }

  .description div p {
    text-transform: uppercase;
    display: flex;
    justify-content: space-between;
  }

  p span {
    font-size: 18px;
    color: green;
    padding: 0 20px 0 0;
  }
</style>
