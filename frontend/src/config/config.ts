export interface ApiEndpoints {
    login: string;
    sources: string;
}

const apiPrefix = 'http://127.0.0.1:8000/';

export const API_ENDPOINTS: ApiEndpoints = {
    login: apiPrefix + 'login/',
    sources: apiPrefix + 'sources/'
};