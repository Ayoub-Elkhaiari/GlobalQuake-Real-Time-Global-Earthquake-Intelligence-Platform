const API=import.meta.env.VITE_API_URL||'http://localhost:8000';
async function request(path){const r=await fetch(`${API}${path}`);if(!r.ok)throw new Error(`API error ${r.status}`);return r.json()}
export const getDashboard=()=>Promise.all([request('/api/v1/earthquakes?page_size=300'),request('/api/v1/statistics/global'),request('/api/v1/statistics/magnitude'),request('/api/v1/statistics/countries'),request('/api/v1/statistics/timeline')]);
export {API,request};
