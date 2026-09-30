import axios from 'axios';

interface ImportMetaEnv {
  readonly VITE_API_URL?: string;
}

interface ImportMetaExtended extends ImportMeta {
  readonly env: ImportMetaEnv;
}

export const api = axios.create({
  baseURL: (import.meta as ImportMetaExtended).env.VITE_API_URL || '/api',
  timeout: 10000,
});
