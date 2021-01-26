import React, { FunctionComponent } from 'react';
import { Shops } from '../../../../common/enums/Shops';
import { IBindingAction } from '../../../../common/models/callback/IBindingAction';
import IconText from '../../../../components/IconText';
import styles from './styles.module.sass';

interface IProps {
  name: string;
  source: string;
  price: string;
  weight: string;
  img: string;
  shop: string;
  onCardClick: IBindingAction;
}

const Card: FunctionComponent<IProps> = ({ name, source, price, weight, img, shop, onCardClick }) => {
  const wrapperStyle = (() => {
    switch (shop) {
      case Shops.Auchan:
        return 'auchanWrapper';
      case Shops.Epicenter:
        return 'epicenterWrapper';
      case Shops.Fozzy:
        return 'fozzyWrapper';
      default:
        return null;
    }
  })();

  return (
    <div className={`${styles.cardWrapper} ${wrapperStyle ? styles[wrapperStyle] : ''}`}>
      <div
        className={`d-flex flex-column text-center justify-content-center ${styles.card}`}
        onClick={onCardClick}
        role="presentation"
      >
        <span className={styles.name}>{name}</span>
        <div className="d-flex mt-2">
          <img src={img} alt="buckwheat" className={styles.img} />
          <div className={styles.infoBlock}>
            <IconText icon="dollar" text={`${price} грн.`} />
            <IconText icon="weight" text={weight} />
            <IconText icon="shop" text={source} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Card;
