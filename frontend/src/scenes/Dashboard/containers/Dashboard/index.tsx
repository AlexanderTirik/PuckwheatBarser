import React, { FunctionComponent, useEffect } from 'react';
import { connect } from 'react-redux';
import { IBindingAction } from '../../../../common/models/callback/IBindingAction';
import Header from '../../../../components/Header';
import { fetchBuckwheatInfoRoutine } from '../../routines/buckwheat';
import BuckwheadCards from '../BuckwheadCards';

interface IProps {
  fetchBuckwheatInfo: IBindingAction;
}

const Dashboard: FunctionComponent<IProps> = ({ fetchBuckwheatInfo }) => {
  useEffect(() => {
    fetchBuckwheatInfo();
  }, []);
  return (
    <>
      <Header />
      <BuckwheadCards />
    </>
  );
};

const mapDispatchToProps = {
  fetchBuckwheatInfo: fetchBuckwheatInfoRoutine
};

export default connect(null, mapDispatchToProps)(Dashboard);
