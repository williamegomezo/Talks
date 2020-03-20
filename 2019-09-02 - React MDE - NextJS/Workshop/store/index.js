import { createStore } from 'redux';

import searchReducer from './reducers/searchReducer';

// const rootReducer = combineReducers({});

const makeStore = (initialState, options) => {
  return createStore(searchReducer, initialState);
};

export default makeStore;
