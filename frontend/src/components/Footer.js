import React from 'react';
import '../styles/Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-col">
          <h4>MediCare Hospital</h4>
          <p>Providing quality healthcare services since 2010.</p>
          <div className="social-links">
            <a href="#facebook">📘</a>
            <a href="#twitter">🐦</a>
            <a href="#linkedin">💼</a>
          </div>
        </div>

        <div className="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li>
              <a href="#services">Services</a>
            </li>
            <li>
              <a href="#doctors">Our Doctors</a>
            </li>
            <li>
              <a href="#careers">Careers</a>
            </li>
            <li>
              <a href="#privacy">Privacy Policy</a>
            </li>
          </ul>
        </div>

        <div className="footer-col">
          <h4>Contact Info</h4>
          <p>📍 123 Medical Avenue, City, State 12345</p>
          <p>📞 1-800-MEDICARE</p>
          <p>✉️ info@medicare.com</p>
        </div>

        <div className="footer-col">
          <h4>Hours</h4>
          <p>Emergency: 24/7</p>
          <p>Clinic: Mon-Fri 9AM-6PM</p>
          <p>Sat-Sun 10AM-4PM</p>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; 2024 MediCare Hospital. All rights reserved.</p>
      </div>
    </footer>
  );
}

export default Footer;
