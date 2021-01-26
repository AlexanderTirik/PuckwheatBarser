
import { all } from 'redux-saga/effects';
import dashboardSaga from '../scenes/Dashboard/sagas';

export default function* rootSaga() {
  yield all([
    dashboardSaga()
  ]);
}
