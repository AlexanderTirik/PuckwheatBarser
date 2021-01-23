import React, { FunctionComponent } from 'react';
import { connect } from 'react-redux';
import { Sort } from '../../../../common/enums/Sort';
import { IBindingCallback } from '../../../../common/models/callback/IBindingCallback';
import { IAppState } from '../../../../common/models/store';
import { fetchBuckwheatInfoRoutine } from '../../routines/buckwheat';
import styles from './styles.module.sass';

interface IProps {
  sort: Sort;
  fetchBuckwheatInfo: IBindingCallback<Sort>;
}

const SortButtons: FunctionComponent<IProps> = ({ sort, fetchBuckwheatInfo }) => (
  <div className={`d-flex justify-content-center ${styles.buttonGroup}`}>
    <button
      type="button"
      className={`${styles.сheap} ${sort === Sort.Asc ? styles.activeCheap : ''}`}
      onClick={() => {
        if (sort !== Sort.Asc) {
          fetchBuckwheatInfo(Sort.Asc);
        }
      }}
    >
      Дешеві
    </button>
    <button
      type="button"
      className={`${styles.noSort} ${sort === Sort.None ? styles.activeNoSort : ''}`}
      onClick={() => {
        if (sort !== Sort.None) {
          fetchBuckwheatInfo(Sort.None);
        }
      }}
    >
      Не сортувати
    </button>
    <button
      type="button"
      className={`${styles.expensive} ${sort === Sort.Desc ? styles.activeExpensive : ''}`}
      onClick={() => {
        if (sort !== Sort.Desc) {
          fetchBuckwheatInfo(Sort.Desc);
        }
      }}
    >
      Дорогі
    </button>
  </div>
);

const mapStateToProps = (state: IAppState) => ({
  sort: state.dashboard.sort
});

const mapDispatchToProps = {
  fetchBuckwheatInfo: fetchBuckwheatInfoRoutine
};

export default connect(mapStateToProps, mapDispatchToProps)(SortButtons);
