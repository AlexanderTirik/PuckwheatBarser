import React, { FunctionComponent } from 'react';
import { ReactComponent as Shop } from '../../assets/icons/shop.svg';
import { ReactComponent as Dollar } from '../../assets/icons/dollar.svg';
import { ReactComponent as Weight } from '../../assets/icons/weight.svg';

export type IconType = 'shop' |
'dollar' |
'weight';

interface IProps {
  icon: IconType;
  className?: string;
}

const Icon: FunctionComponent<IProps> = ({ icon, ...rest }) => {
  switch (icon) {
    case 'shop': return <Shop {...rest} />;
    case 'dollar': return <Dollar {...rest} />;
    case 'weight': return <Weight {...rest} />;
    default: return null;
  }
};

export default Icon;
