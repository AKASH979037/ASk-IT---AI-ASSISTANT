import React from 'react';
import './App.css';
import Header from './components/Header';
import Services from './components/Services';
import Chatbot from './components/Chatbot';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header />

      {/* Hero Section with Chatbot */}
      <section id="home" className="hero-section">
        <div className="hero-container">
          <div className="hero-content">
            <h2>Welcome to MediCare Hospital</h2>
            <p>Your trusted healthcare partner with cutting-edge AI assistance</p>
            <small>💬 Chat with our AI Assistant to get instant answers</small>
          </div>
          <div className="chatbot-wrapper">
            <Chatbot />
          </div>
        </div>
      </section>

      {/* Services Section */}
      <Services />

      {/* Doctors Section */}
      <section id="doctors" className="doctors-section">
        <div className="doctors-container">
          <h2 className="section-title">Our Expert Doctors</h2>
          <p className="section-subtitle">
            Experienced medical professionals dedicated to your health
          </p>
          <div className="doctors-grid">
            {[
              {
                name: 'Dr. Sarah Johnson',
                specialty: 'Cardiology',
                icon: '❤️',
                experience: '15+ years',
              },
              {
                name: 'Dr. Michael Chen',
                specialty: 'Neurology',
                icon: '🧠',
                experience: '12+ years',
              },
              {
                name: 'Dr. Emma Smith',
                specialty: 'Surgery',
                icon: '🔬',
                experience: '18+ years',
              },
              {
                name: 'Dr. James Wilson',
                specialty: 'Pediatrics',
                icon: '👶',
                experience: '10+ years',
              },
            ].map((doctor, index) => (
              <div key={index} className="doctor-card">
                <div className="doctor-icon">{doctor.icon}</div>
                <h3>{doctor.name}</h3>
                <p className="specialty">{doctor.specialty}</p>
                <p className="experience">{doctor.experience}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="about-section">
        <div className="about-container">
          <div className="about-content">
            <h2>About MediCare Hospital</h2>
            <p>
              Founded in 2010, MediCare Hospital has been a beacon of excellence
              in healthcare delivery. With state-of-the-art facilities and a team
              of renowned medical professionals, we're committed to providing the
              highest quality of care.
            </p>
            <ul className="features-list">
              <li>✅ 24/7 Emergency Services</li>
              <li>✅ Modern Medical Equipment</li>
              <li>✅ Expert Medical Team</li>
              <li>✅ Patient-Centric Approach</li>
              <li>✅ Affordable Healthcare</li>
              <li>✅ AI-Powered Assistance</li>
            </ul>
          </div>
          <div className="about-stats">
            <div className="stat-card">
              <h3>50K+</h3>
              <p>Patients Treated</p>
            </div>
            <div className="stat-card">
              <h3>100+</h3>
              <p>Medical Staff</p>
            </div>
            <div className="stat-card">
              <h3>98%</h3>
              <p>Satisfaction Rate</p>
            </div>
            <div className="stat-card">
              <h3>24/7</h3>
              <p>Available Services</p>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="contact-section">
        <div className="contact-container">
          <h2 className="section-title">Get In Touch</h2>
          <p className="section-subtitle">
            We're here to help. Contact us for appointments or inquiries
          </p>
          <div className="contact-grid">
            <div className="contact-card">
              <div className="contact-icon">📍</div>
              <h3>Location</h3>
              <p>123 Medical Avenue</p>
              <p>City, State 12345</p>
            </div>
            <div className="contact-card">
              <div className="contact-icon">📞</div>
              <h3>Phone</h3>
              <p>1-800-MEDICARE</p>
              <p>Available 24/7</p>
            </div>
            <div className="contact-card">
              <div className="contact-icon">✉️</div>
              <h3>Email</h3>
              <p>info@medicare.com</p>
              <p>support@medicare.com</p>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
}

export default App;
