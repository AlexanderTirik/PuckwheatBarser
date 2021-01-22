import React, { FunctionComponent } from 'react';
import IconText from '../../../../components/IconText';
import styles from './styles.module.sass';

interface IProps {
  name: string;
  source: string;
  price: string;
  weight: string;
  img: string;
}

const Card: FunctionComponent<IProps> = ({ name, source, price, weight, img }) => (
  <div className={`d-flex flex-column text-center justify-content-center ${styles.card}`}>
    <span className={styles.name}>{name}</span>
    <div className="d-flex mt-2">
      <img src={img} alt="buckwheat" className={styles.img} />
      <div className={styles.infoBlock}>
        <IconText icon="dollar" text={price} />
        <IconText icon="weight" text={weight} />
        <IconText icon="shop" text={source} />
      </div>
    </div>
  </div>
);

export default Card;
