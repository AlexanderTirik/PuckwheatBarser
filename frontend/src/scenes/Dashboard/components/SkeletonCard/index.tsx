import React, { FunctionComponent } from 'react';
import Skeleton from 'react-loading-skeleton';
import styles from './styles.module.sass';

const SkeletonCard: FunctionComponent = () => (
  <div className={`${styles.card} justify-content-center`}>
    <Skeleton width={250} className="ml-3" />
    <div className="d-flex">
      <Skeleton width={70} height={90} />
      <div className="d-flex flex-column ml-2">
        <Skeleton width={70} height={20} className="mb-1" />
        <Skeleton width={70} height={20} className="mb-1" />
        <Skeleton width={70} height={20} className="mb-1" />
      </div>
    </div>
  </div>
);

export default SkeletonCard;
