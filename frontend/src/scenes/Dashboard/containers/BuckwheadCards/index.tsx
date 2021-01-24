import React, { FunctionComponent } from 'react';
import { connect } from 'react-redux';
import { generateId } from '../../../../common/helpers/idHelper';
import { IBuckwheatData } from '../../../../common/models/IBuckwheatData';
import { IAppState } from '../../../../common/models/store';
import Card from '../../components/Card';
import SkeletonCard from '../../components/SkeletonCard';

interface IProps {
  buckwheatData: IBuckwheatData[];
  isLoading: boolean[];
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
        isLoading.length
          ? Array.from(Array(20)).map(() => <SkeletonCard key={generateId()} />)
          : buckwheatData.map(data => (
            <Card
              key={generateId()}
              shop={data.shop}
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
