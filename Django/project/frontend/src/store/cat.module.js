import ApiService from '../services/api.service'
import {
  FETCH_CATS,
  FETCH_A_CAT
} from './actions.type'
import {
  FETCH_START,
  FETCH_END,
  SET_A_CAT,
  SET_CATS,
  SET_ERROR
} from './mutations.type'

ApiService.init();

const state = {
  // TODO: a list of state related to cats
  cats: [],
  cat: {},
  errors: {},
  loading: false
};

const getters = {
  // TODO: define method to access state value
  currentCat(state) {
    return state.cat;
  },
  cats(state) {
    return state.cats;
  },
  isLoading(state) {
    return state.loading;
  }

};

const actions = {
  // TODO: define actions like FETCH_A_CAT
  [FETCH_CATS](context, payload) {
    console.log("Getting cats");
    context.commit(FETCH_START);
    return ApiService
      .get('cats')
      .then(({data}) => {
        console.log(data);
        console.log(data.cats);
        context.commit(SET_CATS, data.cats);
        context.commit(FETCH_END)
      })
      .catch(({response}) => {
        context.commit(SET_ERROR, response.data.errors)

      })
  },
  [FETCH_A_CAT](context, payload) {
    console.log("Getting A cat");

    context.commit(FETCH_START);
    const {cat_id} = payload;
    return ApiService
      .get(`cats/${cat_id}`)
      .then(({data}) => {
        context.commit(SET_A_CAT, data.cats);
        context.commit(FETCH_END)
      })
      .catch(({response}) => {
        context.commit(SET_ERROR, response.data.errors)
      })
  }
};

const mutations = {
  // TODO: define mutations to redefine state value
  [FETCH_START](state) {
    state.loading = true;
  },
  [FETCH_END](state) {
    state.loading = false;
  },
  [SET_CATS](state, pCats) {
    state.cats = pCats;
    state.errors = {};
  },
  [SET_A_CAT](state, pCat) {
    state.cat = pCat;
    state.errors = {};
  },
  [SET_ERROR](state) {
    state.errors = errors;
  }

};

export default {
  state,
  getters,
  actions,
  mutations
};
