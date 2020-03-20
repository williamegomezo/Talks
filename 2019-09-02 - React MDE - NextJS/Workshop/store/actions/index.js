import {
  CHANGE_SEARCH
} from './action-types';

export function changeSearch(payload) {
  return { type: CHANGE_SEARCH, payload };
}
