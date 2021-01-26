import { IBuckwheatData } from '../../../common/models/IBuckwheatData';
import { fetchBuckwheatInfo } from '../../../services/buckwheatService';
import { fetchBuckwheatInfoRoutine } from '../routines/buckwheat';
import { all, put, call, takeEvery } from 'redux-saga/effects';
import { Routine } from 'redux-saga-routines';

function* fetchBuckwheatInfoRequest({ payload }: Routine<any>) {
  try {
    const buckwheatInfo: IBuckwheatData = yield call(fetchBuckwheatInfo, payload);
    yield put(fetchBuckwheatInfoRoutine.success(buckwheatInfo));
  } catch (error) {
    yield put(fetchBuckwheatInfoRoutine.failure());
  }
}

function* watchFetchUserRequest() {
  yield takeEvery(fetchBuckwheatInfoRoutine.TRIGGER, fetchBuckwheatInfoRequest);
}

export default function* dashboardSaga() {
  yield all([
    watchFetchUserRequest()
  ]);
}
