import React, { FunctionComponent } from 'react';
import styles from './styles.module.sass';
import { Shops } from '../../common/enums/Shops';

interface IProps {
  shop: Shops;
  color: string;
}

const ShopColor: FunctionComponent<IProps> = ({ shop, color }) => (
  <div className="d-flex ml-4 align-items-center">
    <div style={{ backgroundColor: color }} className={styles.colorBlock} />
    <span className={styles.shop}>{` - ${shop}`}</span>
  </div>
);

export default ShopColor;
