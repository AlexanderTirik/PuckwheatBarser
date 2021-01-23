import React, { FunctionComponent } from 'react';
import { connect } from 'react-redux';
import { IBuckwheatData } from '../../../../common/models/IBuckwheatData';
import { IAppState } from '../../../../common/models/store';
import Card from '../../components/Card';
import SkeletonCard from '../../components/SkeletonCard';

interface IProps {
  buckwheatData: IBuckwheatData[];
  isLoading: boolean;
}

const BuckwheatCards: FunctionComponent<IProps> = ({ buckwheatData, isLoading }) => {
  const onCardClick = (url: string) => {
    const win = window.open(url, '_blank');
    if (win != null) {
      win.focus();
    }
  };

  return (
    <div className="d-flex flex-wrap justify-content-center">
      {
        isLoading
          ? Array.from(Array(20)).map(() => <SkeletonCard />)
          : null
      }
      {
        buckwheatData.map(data => (
          <Card
            price={data.price}
            name={data.name}
            source={data.source}
            weight={data.weight}
            img={data.imgUrl}
            onCardClick={() => onCardClick(data.productUrl)}
          />
        ))
      }
    </div>
  );
};

const mapStateToProps = (state: IAppState) => ({
  buckwheatData: state.dashboard.buckwheatData,
  isLoading: state.dashboard.isLoading
});

export default connect(mapStateToProps)(BuckwheatCards);
