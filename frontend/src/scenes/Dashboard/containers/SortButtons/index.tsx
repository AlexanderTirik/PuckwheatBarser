import React, { FunctionComponent } from 'react';
import { connect } from 'react-redux';
import { Sort } from '../../../../common/enums/Sort';
import { IBindingCallback } from '../../../../common/models/callback/IBindingCallback';
import { IAppState } from '../../../../common/models/store';
import { fetchBuckwheatInfoRoutine } from '../../routines/buckwheat';
import styles from './styles.module.sass';

interface IProps {
  sort: Sort;
  isLoading: boolean[];
  fetchBuckwheatInfo: IBindingCallback<Sort>;
}

const SortButtons: FunctionComponent<IProps> = ({ sort, isLoading, fetchBuckwheatInfo }) => (
  <div className={`d-flex justify-content-center ${styles.buttonGroup} ${isLoading.length ? styles.loading : ''}`}>
    <button
      type="button"
      className={`${styles.сheap} ${sort === Sort.Asc ? styles.activeCheap : ''}
      `}
      onClick={() => {
        if (sort !== Sort.Asc && !isLoading.length) {
          fetchBuckwheatInfo(Sort.Asc);
        }
      }}
    >
      Дешеві
    </button>
    <button
      type="button"
      className={`${styles.noSort} ${sort === Sort.None ? styles.activeNoSort : ''}
      `}
      onClick={() => {
        if (sort !== Sort.None && !isLoading.length) {
          fetchBuckwheatInfo(Sort.None);
        }
      }}
    >
      Не сортувати
    </button>
    <button
      type="button"
      className={`${styles.expensive} ${sort === Sort.Desc ? styles.activeExpensive : ''}
      `}
      onClick={() => {
        if (sort !== Sort.Desc && !isLoading.length) {
          fetchBuckwheatInfo(Sort.Desc);
        }
      }}
    >
      Дорогі
    </button>
  </div>
);

const mapStateToProps = (state: IAppState) => ({
  sort: state.dashboard.sort,
  isLoading: state.dashboard.isLoading
});

const mapDispatchToProps = {
  fetchBuckwheatInfo: fetchBuckwheatInfoRoutine
};

export default connect(mapStateToProps, mapDispatchToProps)(SortButtons);
