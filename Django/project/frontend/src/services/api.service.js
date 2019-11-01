import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import {API_URL} from './config'

const ApiService = {
  init() {
    console.log("Initilizing ...");
    Vue.use(VueAxios, axios);
    Vue.axios.defaults.baseURL = API_URL;
  },

  get(resource) {
    return Vue.axios
      .get(`${resource}/`)
      .catch((error) => {
        throw new Error(`ApiService ${error}`);
      })
  },
};
export default ApiService;
