import React, { FunctionComponent, useEffect } from 'react';
import { connect } from 'react-redux';
import Header from '../../../../components/Header';
import SortButtons from '../SortButtons';
import { fetchBuckwheatInfoRoutine } from '../../routines/buckwheat';
import BuckwheadCards from '../BuckwheadCards';
import { IBindingCallback } from '../../../../common/models/callback/IBindingCallback';
import { Sort } from '../../../../common/enums/Sort';

interface IProps {
  fetchBuckwheatInfo: IBindingCallback<Sort>;
}

const Dashboard: FunctionComponent<IProps> = ({ fetchBuckwheatInfo }) => {
  useEffect(() => {
    fetchBuckwheatInfo(Sort.None);
  }, [fetchBuckwheatInfo]);
  return (
    <>
      <Header />
      <SortButtons />
      <BuckwheadCards />
    </>
  );
};

const mapDispatchToProps = {
  fetchBuckwheatInfo: fetchBuckwheatInfoRoutine
};

export default connect(null, mapDispatchToProps)(Dashboard);
