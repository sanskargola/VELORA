/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#2563EB',
        secondary: '#10B981',
        accent: '#F59E0B',
        background: '#0F172A',
        surface: '#111827',
        text: '#F8FAFC'
      },
      boxShadow: {
        glow: '0 0 40px rgba(37, 99, 235, 0.25)'
      }
    }
  },
  plugins: []
};
