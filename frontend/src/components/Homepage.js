import React from 'react';
import { useNavigate } from 'react-router-dom';   // ✅ add this
import './Homepage.css';

function Homepage() {
  const navigate = useNavigate();   // ✅ hook

  return (
    <div className="homepage-container">

      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-text">
          <h1>Offensive Text Detection</h1>
          <p>Analyze text across languages and get deep insights on offensive patterns.</p>

          {/* ✅ Navigate on click */}
          <button
            className="btn-gradient"
            onClick={() => navigate('/dashboard')}
          >
            Get Started
          </button>
        </div>

        <div className="hero-image">
          <img
            src="https://img.icons8.com/ios-filled/200/ffffff/artificial-intelligence.png"
            alt="AI Illustration"
          />
        </div>
      </section>

      {/* Features Section */}
      <section className="features-section">
        <h2>Core Features</h2>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">🧠</div>
            <h3>AI-Powered Detection</h3>
            <p>State-of-the-art ML models to detect offensive text accurately.</p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">🌐</div>
            <h3>Bilingual Support</h3>
            <p>Works for Tamil-English code-mixed content and more languages.</p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📊</div>
            <h3>Insights & Analytics</h3>
            <p>Visualize patterns and features extracted from the dataset.</p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>Fast & Interactive</h3>
            <p>Quick predictions and an easy-to-use interactive frontend.</p>
          </div>
        </div>
      </section>

      {/* Dataset Section */}
      <section className="dataset-section">
        <div className="dataset-content">
          <h2>Dataset Insights</h2>
          <p>
            Explore frequent offensive words, stylometric features, and the patterns
            that distinguish offensive and non-offensive content.
          </p>

          {/* Optional navigation */}
          <button
            className="btn-outline"
            onClick={() => navigate('/dashboard')}
          >
            Explore Dataset
          </button>
        </div>
      </section>

    </div>
  );
}

export default Homepage;
