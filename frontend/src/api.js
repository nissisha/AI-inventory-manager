import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const getItems = () => axios.get(`${API_URL}/items`);
export const createItem = (item) => axios.post(`${API_URL}/items`, item);
export const deleteItem = (id) => axios.delete(`${API_URL}/items/${id}`);
export const getRecommendation = (id) => axios.get(`${API_URL}/ai-recommendation/${id}`);