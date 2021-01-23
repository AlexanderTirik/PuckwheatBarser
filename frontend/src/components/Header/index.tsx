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
      <ShopColor shop={Shops.Fozzy} color="#fffcf7" />
      <ShopColor shop={Shops.Epicenter} color="#f8f0ff" />
      <ShopColor shop={Shops.Auchan} color="#ebfff2" />
    </div>
  </header>
);

export default Header;
