// API Configuration
// Update the API endpoint here when your backend is ready

const API_CONFIG = {
  // Change this to your backend API endpoint
  CHAT_API_ENDPOINT: process.env.REACT_APP_API_URL || 'http://localhost:8000/hello',
  
  // API timeout in milliseconds
  TIMEOUT: 30000,
  
  // Hospital name for branding
  HOSPITAL_NAME: 'MediCare Hospital',
  
  // Hospital contact info
  HOSPITAL_INFO: {
    phone: '1-800-MEDICARE',
    email: 'info@medicare.com',
    address: '123 Medical Avenue, City, State 12345',
    emergencyPhone: '911',
  },
};

export default API_CONFIG;
