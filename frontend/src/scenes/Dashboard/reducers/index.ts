import { Routine } from 'redux-saga-routines';
import { Sort } from '../../../common/enums/Sort';
import { IBuckwheatData } from '../../../common/models/IBuckwheatData';
import { fetchBuckwheatInfoRoutine } from '../routines/buckwheat';

export interface IDashboardState {
  isLoading: boolean[];
  buckwheatData: IBuckwheatData[];
  sort: Sort;
}

const initialState: IDashboardState = {
  isLoading: [],
  buckwheatData: [],
  sort: Sort.None
};

const reducer = (state = initialState, { type, payload }: Routine<any>): IDashboardState => {
  switch (type) {
    case fetchBuckwheatInfoRoutine.TRIGGER: {
      return {
        ...state,
        sort: payload || Sort.None,
        isLoading: [...state.isLoading, true]
      };
    }
    case fetchBuckwheatInfoRoutine.SUCCESS: {
      const isLoadingCopy = [...state.isLoading];
      isLoadingCopy.pop();
      return {
        ...state,
        buckwheatData: payload.sort && state.sort === payload.sort ? payload.buckwheatData : state.buckwheatData,
        isLoading: isLoadingCopy
      };
    }
    case fetchBuckwheatInfoRoutine.FAILURE: {
      const isLoadingCopy = [...state.isLoading];
      isLoadingCopy.pop();
      return {
        ...state,
        isLoading: isLoadingCopy
      };
    }
    default:
      return state;
  }
};

export default reducer;
