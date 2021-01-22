import api from '../common/helpers/apiHelper';

export const fetchBuckwheatInfo = () => api.get('/get_data');
