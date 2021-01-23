import { Routine } from 'redux-saga-routines';
import { Sort } from '../../../common/enums/Sort';
import { IBuckwheatData } from '../../../common/models/IBuckwheatData';
import { fetchBuckwheatInfoRoutine } from '../routines/buckwheat';

export interface IDashboardState {
  isLoading: boolean;
  buckwheatData: IBuckwheatData[];
  sort: Sort;
}

const initialState: IDashboardState = {
  isLoading: false,
  buckwheatData: [],
  sort: Sort.None
};

const reducer = (state = initialState, { type, payload }: Routine<any>): IDashboardState => {
  switch (type) {
    case fetchBuckwheatInfoRoutine.TRIGGER: {
      return {
        ...state,
        sort: payload,
        isLoading: true
      };
    }
    case fetchBuckwheatInfoRoutine.SUCCESS: {
      return {
        ...state,
        buckwheatData: payload,
        isLoading: false
      };
    }
    case fetchBuckwheatInfoRoutine.FAILURE: {
      return {
        ...state,
        isLoading: false
      };
    }
    default:
      return state;
  }
};

export default reducer;
