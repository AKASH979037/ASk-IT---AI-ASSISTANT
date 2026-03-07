# MediCare Hospital - AI Chatbot Website

A professional hospital website built with React and featuring an AI-powered chatbot for patient assistance and inquiries.

## 📋 Project Structure

```
frontend/
├── public/
│   └── index.html          # Main HTML file
├── src/
│   ├── components/
│   │   ├── Header.js       # Navigation header
│   │   ├── Chatbot.js      # AI Chatbot component
│   │   ├── Services.js     # Hospital services section
│   │   └── Footer.js       # Footer component
│   ├── styles/
│   │   ├── Header.css      # Header styling
│   │   ├── Chatbot.css     # Chatbot styling
│   │   ├── Services.css    # Services section styling
│   │   └── Footer.css      # Footer styling
│   ├── App.js              # Main app component
│   ├── App.css             # Global styles
│   └── index.js            # React entry point
├── package.json            # Dependencies
└── README.md              # This file
```

## ✨ Features

### 🏥 Hospital Website
- **Professional Header** - Easy navigation with responsive menu
- **Hero Section** - Eye-catching landing with integrated chatbot
- **Services Section** - Display of hospital departments and services
- **Doctors Section** - Showcase of medical professionals
- **About Section** - Hospital information and statistics
- **Contact Section** - Multiple contact options
- **Footer** - Complete footer with links and info

### 🤖 AI Chatbot
- **Real-time Chat** - Interactive messaging interface
- **Message History** - Full conversation history displayed
- **Typing Indicator** - Visual feedback when bot is responding
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Error Handling** - Graceful error messages
- **API Integration** - Ready to connect with backend

## 🎨 Design Features

- **Modern UI** - Clean, professional gradient design
- **Smooth Animations** - Fade-in and hover effects
- **Responsive Layout** - Mobile-first approach
- **Accessibility** - Semantic HTML and keyboard navigation
- **Color Scheme**:
  - Primary: Purple gradient (#667eea → #764ba2)
  - Secondary: Light gray (#f8f9fa)
  - Accent: Red (#ff6b6b)

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm start
```

The app will open at `http://localhost:3000`

### Build for Production
```bash
npm run build
```

## 🔌 Backend API Integration

The chatbot is configured to call the backend API at `http://localhost:5000/api/chat`

### Expected API Response Format
```json
{
  "response": "Your answer here"
}
```

### API Request Format
```json
{
  "message": "User's question or message"
}
```

To use your backend API:
1. Update the API endpoint in [Chatbot.js](src/components/Chatbot.js) line 52
2. Ensure your backend is running on the specified port
3. Handle CORS if backend is on different origin

## 📱 Responsive Breakpoints

- **Desktop**: 1024px and above
- **Tablet**: 768px - 1023px  
- **Mobile**: Below 768px

## 🎯 Component Details

### Chatbot Component
- Scrollable message container
- Auto-scroll to latest message
- Loading state with typing indicator
- Error handling for API failures
- Timestamp for each message

### Header Component
- Sticky navigation
- Responsive hamburger menu
- Quick appointment booking button
- Hospital branding

### Services Component
- 6 medical departments
- Icon cards with descriptions
- Hover animations

### Documentation

Each component is self-contained and can be customized:
- **Header.js** - Update logo, navigation links, hospital name
- **Chatbot.js** - Change API endpoint, customize prompts
- **Services.js** - Add/remove services, modify icons
- **Footer.js** - Update contact information
- **CSS Files** - Modify colors, fonts, spacing

## 🔧 Customization

### Change Hospital Name
Update in:
- [Header.js](src/components/Header.js) line 7
- [Chatbot.js](src/components/Chatbot.js) line 78

### Change Colors
Update in CSS files or App.css:
- Primary gradient: `#667eea` and `#764ba2`
- Secondary colors in respective component styles

### Update Contact Information
Modify [Footer.js](src/components/Footer.js) with your hospital details

## 📦 Dependencies

- **react**: ^18.2.0 - UI library
- **react-dom**: ^18.2.0 - DOM rendering
- **axios**: ^1.4.0 - HTTP client (optional, using fetch currently)
- **react-scripts**: 5.0.1 - Build tools

## 🐛 Troubleshooting

### Chatbot not connecting to backend
- Ensure backend is running on `http://localhost:5000`
- Check CORS settings in backend
- Verify API endpoint in Chatbot.js

### Styles not loading
- Clear browser cache
- Restart development server
- Check CSS file paths in components

### Mobile responsiveness issues
- Test in Chrome DevTools device emulation
- Check viewport meta tag in index.html
- Verify media queries in CSS files

## 📞 Support

For hospital-specific customizations or API integration help, refer to the component files with inline comments.

## 📄 License

This project is created for MediCare Hospital.

---

**Ready to connect with backend?** 
Provide your API endpoint and response format, and the chatbot will be fully functional!
