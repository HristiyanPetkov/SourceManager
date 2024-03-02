export interface ApiEndpoints {
    sources: string;
    user: string;
}

const apiPrefix = 'http://127.0.0.1:8000/';

export const API_ENDPOINTS: ApiEndpoints = {
    sources: apiPrefix + 'sources/',
    user: apiPrefix + 'users/'
};