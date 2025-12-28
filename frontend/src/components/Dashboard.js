import React from "react";
import { useNavigate } from "react-router-dom";
import "./Dashboard.css";

function Dashboard() {
  const navigate = useNavigate();

  return (
    <div className="dashboard-container">
      <h1 className="dashboard-title">Offensive Text Detection Dashboard</h1>
      <p className="dashboard-subtitle">
        Select a module to explore analysis and insights
      </p>

      <div className="card-grid">

        <div className="dashboard-card" onClick={() => navigate("/analyze")}>
          <div className="card-icon">🧠</div>
          <h3>Analyze Text</h3>
          <p>
            Detect offensive content and perform word-level analysis on input text.
          </p>
        </div>

        <div className="dashboard-card" onClick={() => navigate("/stylometry")}>
          <div className="card-icon">📊</div>
          <h3>Stylometric Features</h3>
          <p>
            View extracted linguistic and stylometric features from the dataset.
          </p>
        </div>

        <div className="dashboard-card" onClick={() => navigate("/dataset")}>
          <div className="card-icon">🌐</div>
          <h3>Dataset Insights</h3>
          <p>
            Explore dataset statistics, language distribution, and patterns.
          </p>
        </div>

      </div>
    </div>
  );
}

export default Dashboard;
