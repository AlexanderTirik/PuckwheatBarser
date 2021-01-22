import React, { FunctionComponent } from 'react';
import Icon, { IconType } from '../Icon';
import styles from './styles.module.sass';

interface IProps {
  icon: IconType;
  text: string;
}

const IconText: FunctionComponent<IProps> = ({ icon, text }) => (
  <div className="d-flex flex-row align-items-center iconText">
    <Icon icon={icon} className={styles.icon} />
    <span>{text}</span>
  </div>
);

export default IconText;
