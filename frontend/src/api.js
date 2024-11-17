import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

//Esta variable va a contener el url base de nuestra aplicación
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

api.interceptors.request.use(
  //Esta función se encarga de añadir a la cabecera HTTP el token de autentificación
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  //Esta función se encarga de rechazar promesa si hay algún error
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
