import { Sort } from '../common/enums/Sort';
import api from '../common/helpers/apiHelper';

export const fetchBuckwheatInfo = (sort?: Sort) => api.get('/get_data', { sort });
