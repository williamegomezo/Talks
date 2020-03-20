import { CHANGE_SEARCH } from '../actions/action-types';

const initialState = {
  search: ''
};

function searchReducer(state = initialState, action) {
  if (action.type === CHANGE_SEARCH) {
    return {
      ...state,
      search: action.payload
    };
  }
  return state;
}

export default searchReducer;
