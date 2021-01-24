import React, { FunctionComponent } from 'react';
import { Shops } from '../../common/enums/Shops';
import ShopColor from '../ShopColor';
import styles from './styles.module.sass';

const Header: FunctionComponent = () => (
  <header className={`${styles.header} d-flex align-items-center justify-content-around`}>
    <span className={styles.headerName}>
      Puckwheat Barser
    </span>
    <div className={`d-flex ${styles.shopColor}`}>
      <ShopColor shop={Shops.Fozzy} color="#fff9c9" />
      <ShopColor shop={Shops.Epicenter} color="#e8e3ff" />
      <ShopColor shop={Shops.Auchan} color="#ffd1c9" />
    </div>
  </header>
);

export default Header;
