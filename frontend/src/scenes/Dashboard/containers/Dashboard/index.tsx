import React, { FunctionComponent, useEffect } from 'react';
import { connect } from 'react-redux';
import { IBindingAction } from '../../../../common/models/callback/IBindingAction';
import { fetchBuckwheatInfoRoutine } from '../../routines/buckwheat';
import styles from './styles.module.sass';

interface IProps {
  fetchBuckwheatInfo: IBindingAction;
}

const Dashboard: FunctionComponent<IProps> = ({ fetchBuckwheatInfo }) => {
  useEffect(() => {
    fetchBuckwheatInfo();
  }, []);
  return (
    <>
      <header className={`d-flex justify-content-center ${styles.header}`}>Puckwheat Barser</header>

    </>
  );
};

const mapDispatchToProps = {
  fetchBuckwheatInfo: fetchBuckwheatInfoRoutine
};

export default connect(null, mapDispatchToProps)(Dashboard);
