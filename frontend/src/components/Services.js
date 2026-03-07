import React from 'react';
import '../styles/Services.css';

function Services() {
  const services = [
    {
      id: 1,
      icon: '🏨',
      title: 'Emergency Care',
      description: 'Available 24/7 for urgent and emergency medical needs.',
    },
    {
      id: 2,
      icon: '👨‍⚕️',
      title: 'Surgery',
      description: 'Expert surgical team with state-of-the-art equipment.',
    },
    {
      id: 3,
      icon: '🧬',
      title: 'Diagnostics',
      description: 'Advanced diagnostic services with quick results.',
    },
    {
      id: 4,
      icon: '🏃',
      title: 'Cardiology',
      description: 'Comprehensive heart care and treatment services.',
    },
    {
      id: 5,
      icon: '🧠',
      title: 'Neurology',
      description: 'Specialized care for nervous system disorders.',
    },
    {
      id: 6,
      icon: '👶',
      title: 'Pediatrics',
      description: 'Child healthcare and developmental services.',
    },
  ];

  return (
    <section id="services" className="services-section">
      <div className="services-container">
        <h2 className="section-title">Our Services</h2>
        <p className="section-subtitle">
          We offer comprehensive healthcare services to meet your needs
        </p>

        <div className="services-grid">
          {services.map((service) => (
            <div key={service.id} className="service-card">
              <div className="service-icon">{service.icon}</div>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Services;
